#-*- coding:utf-8 -*-
# 本程序用于将mvcd文件转换为mcfunction
import sys
print("This is mvcd2mcf v1.0")
a=sys.argv[0]
codes=[]
outname=""
if len(sys.argv)==1:
	print("python mvcd2mcf.py inputfilepath [outputfilename]")
	exit()
elif len(sys.argv)==2:
	s=""
	with open(sys.argv[1],'r',encoding='utf-8') as f:
		s=f.read()
	d=s.split("\n")
	for i in d:
		codes.append(i.strip())
	outname="output.mcfunction"
elif len(sys.argv)==3:
	s=""
	with open(sys.argv[1],'r',encoding='utf-8') as f:
		s=f.read()
	d=s.split("\n")
	for i in d:
		codes.append(i.strip())
	outname=a=sys.argv[2]+".mcfunction"


mat="minecraft:white_concrete"
a=input("输入材质(默认为minecraft:white_concrete)：")
print("载入成功，正在分析...")
if a.strip()!="":
	mat=a.strip()
cubenum=float(codes[2])
cubes=[]
i=3
while i<3+cubenum:
	cubes.append(codes[i])
	i=i+1

print("分析完成，正在写出...")
with open(outname,'w',encoding='utf-8') as f:
		for i in cubes:
			k=i.split(" ")
			txt=f"setblock ~{k[0]} ~{k[1]} ~{k[2]} {mat}\n"
			f.write(txt)
print("写出完成...")

