#-*- coding:utf-8 -*-
#version v1.0 mvcd-file
# 本程序用于将MagicVoxel导出的Ply模型转换为用于我的世界的模型
import numpy as np
import sys
print("This is ply2mvcd v1.0")
a=sys.argv[0]
codes=[]
outname=""
if len(sys.argv)==1:
	print("python mv2mc.py inputfilepath [outputfilename]")
	exit()
elif len(sys.argv)==2:
	s=""
	with open(sys.argv[1],'r',encoding='utf-8') as f:
		s=f.read()
	d=s.split("\n")
	for i in d:
		codes.append(i.strip())
	outname="output.mvcd"
elif len(sys.argv)==3:
	s=""
	with open(sys.argv[1],'r',encoding='utf-8') as f:
		s=f.read()
	d=s.split("\n")
	for i in d:
		codes.append(i.strip())
	outname=a=sys.argv[2]+".mvcd"

if codes[0]!="ply":
	print("headfile error!!")
	exit()

class Color(object):
	"""docstring for Color"""
	def __init__(self,r,g,b):
		super(Color, self).__init__()
		self.r=r
		self.g=g
		self.b=b
	def __str__(self):
		return str(self.r)+" "+str(self.g)+" "+str(self.b)
		
class Cube(object):
	"""docstring for Cube"""
	def __init__(self,x,y,z,color):
		super(Cube, self).__init__()
		self.x=x
		self.y=y
		self.z=z
		self.color=color
	def __eq__(self,otherCube):
		if self.x==otherCube.x and self.y==otherCube.y and self.z==otherCube.z:
			return True
		else:
			return False
	def __str__(self):
		return str(self.x)+" "+str(self.z)+" "+str(self.y)+" "+str(self.color)
	
vernum=int(codes[4].split(" ")[2]) #顶点数量
fnum=int(codes[11].split(" ")[2]) #面片数量
vertexs=[]
faces=[]
colors=[]
cubes=[]

i=14
while i<14+vernum:
	x=codes[i].split(" ")
	l=[float(x[0]),float(x[1]),float(x[2])]
	vertexs.append(l)
	l=[float(x[3]),float(x[4]),float(x[5])]
	colors.append(l)
	i=i+1

while  i<14+vernum+fnum:
	x=codes[i].split(" ")
	l=[int(x[1]),int(x[2]),int(x[3]),int(x[4])]
	faces.append(l)
	i=i+1

def isExist(cuber):
	global cubes
	for i in cubes:
		if cuber==i:
			return True
	return False

#通过面直接计算体的位置
def f2v(p1,p2,p3):
	global cubes,vertexs,colors
	x1=np.array(vertexs[p1])
	x2=np.array(vertexs[p2])
	x3=np.array(vertexs[p3])
	x2x1=x2-x1
	x3x2=x3-x2
	vec=np.cross(x2x1,x3x2)
	vec=vec*-0.5
	y=(x1+x3)/2+vec
	cub=Cube(y[0],y[1],y[2],Color(colors[p1][0],colors[p1][1],colors[p1][2]))
	if isExist(cub)== False:
		cubes.append(cub)


if __name__ == '__main__':
	k=1
	for i in faces:
		print(f"tasks:  {k}faces / {len(faces)}faces   schedule: {k/len(faces)*100}%")
		f2v(i[0],i[1],i[2])
		k=k+1
	print("Done. Resetting Position...")
	z=[]
	x=[]
	y=[]
	print("Please wait..")
	for i in cubes:
		z.append(i.z)
		x.append(i.x)
		y.append(i.y)

	minz=min(z)
	minx=min(x)
	miny=min(y)
	cz=minz-0
	cx=minx-1
	cy=miny-1

	print("Everything will be ok!")
	for i in cubes:
		i.z=float(i.z-cz)
		i.x=float(i.x-cx)
		i.y=float(i.y-cy)

	print("It's time to enjoy! Outputting ...")
	with open(outname,'w',encoding='utf-8') as f:
		f.write("MagicaVoxelCubeData\nv1.0\n")
		f.write(str(len(cubes))+"\n")
		for i in cubes:
			f.write(str(i)+"\n")

	print("Successfully Output！！")





