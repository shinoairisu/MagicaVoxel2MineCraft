#-*- coding:utf-8 -*-
# 本程序用于将mvcd文件转换为mcfunction,并使用mc中相近颜色方块作为材料
import sys
import numpy as np
import math
print("This is mvcd2cmcf v1.0")
a=sys.argv[0]
codes=[]
outname=""
if len(sys.argv)==1:
	print("python mvcd2cmcf.py inputfilepath [outputfilename]")
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
exs={}
#色盘区域  开始#########################
###从color.py中获取颜色文本后放置于此处####
#######################################
#######################################
exs["minecraft:black_wool"]=[29, 29, 33] #黑色
exs["minecraft:red_wool"]=[176, 46, 38]  #红色
exs["minecraft:green_wool"]=[94, 124, 22]  #绿色
exs["minecraft:brown_wool"]=[131, 84, 50]  #棕色
exs["minecraft:blue_wool"]=[60, 68, 170]  #蓝色
exs["minecraft:purple_wool"]=[137, 50, 184]  #紫色
exs["minecraft:cyan_wool"]=[22, 156, 156]  #青色
exs["minecraft:light_gray_wool"]=[157, 157, 151] #淡灰色
exs["minecraft:gray_wool"]=[71, 79, 82] #灰色
exs["minecraft:pink_wool"]=[243, 139, 170] #粉红色
exs["minecraft:lime_wool"]=[128, 199, 31]  #黄绿色
exs["minecraft:yellow_wool"]=[254, 216, 61]  #黄色
exs["minecraft:light_blue_wool"]=[58, 179, 218]  #淡蓝色
exs["minecraft:magenta_wool"]=[199, 78, 189]  #品红色
exs["minecraft:orange_wool"]=[249, 128, 29]  #橙色
exs["minecraft:white_wool"]=[249, 255, 254]  #白色
#####################################
#####################################
#####################################
#色盘区域 结束


print("载入成功，正在分析...")
if a.strip()!="":
	mat=a.strip()
cubenum=int(codes[2])
cubes=[]
colors=[]
mat=[]
i=3
while i<3+cubenum:
	e=codes[i].split(" ")
	cubes.append([e[0],e[1],e[2]])
	colors.append([e[3],e[4],e[5]])
	i=i+1
print("解析完成，正在筛选合适的砖块...")
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*60
        else:
            h = ((g-b)/m)*60 + 360
    elif mx == g:
        h = ((b-r)/m)*60 + 120
    elif mx == b:
        h = ((r-g)/m)*60 + 240
    if mx == 0:
        s = 0
    else:
        s = m/mx
    v = mx
    H = h / 2
    S = s * 255.0
    V = v * 255.0
    return [H, S, V]

def HSVDistance(hsv_1,hsv_2):
    H_1,S_1,V_1 = hsv_1
    H_2,S_2,V_2 = hsv_2
    R=100
    angle=30
    h = R * math.cos(angle / 180 * math.pi)
    r = R * math.sin(angle / 180 * math.pi)
    x1 = r * V_1 * S_1 * math.cos(H_1 / 180 * math.pi);
    y1 = r * V_1 * S_1 * math.sin(H_1 / 180 * math.pi);
    z1 = h * (1 - V_1);
    x2 = r * V_2 * S_2 * math.cos(H_2 / 180 * math.pi);
    y2 = r * V_2 * S_2 * math.sin(H_2 / 180 * math.pi);
    z2 = h * (1 - V_2);
    dx = x1 - x2;
    dy = y1 - y2;
    dz = z1 - z2;
    return math.sqrt(dx * dx + dy * dy + dz * dz);

def hsvdis2(h1,h2):
	vector1 = np.array([h1[0],h1[1],h1[2]])
	vector2 = np.array([h2[0],h2[1],h2[2]])
	op3=np.sum(np.abs(vector1-vector2))
	return op3

def distance(v1,v2):
	h1=rgb2hsv(v1[0],v1[1],v1[2])
	h2=rgb2hsv(v2[0],v2[1],v2[2])
	return hsvdis2(h1,h2)

#将颜色数组传入,返回合适的砖块名称,输入颜色
def selcolors(rgb):
	global exs
	v1=np.array([float(rgb[0]),float(rgb[1]),float(rgb[2])])
	dis=[]
	name=[]
	for i in exs:
		v2=np.array([float(exs[i][0]),float(exs[i][1]),float(exs[i][2])])
		dis.append(distance(v1,v2))
		name.append(i)
	return name[dis.index(min(dis))]

if __name__ == '__main__':
	j=1
	for i in colors:
		print(f"tasks:  {j}Cubes / {len(colors)}Cubes   schedule: {j/len(colors)*100}%")
		mat.append(selcolors(i))
		j=j+1
	print("所有方块均已选择完毕，正在编写mcfunction")
	with open(outname,'w',encoding='utf-8') as f:
		for i in range(0,len(cubes)-1):
			txt=f"setblock ~{cubes[i][0]} ~{cubes[i][1]} ~{cubes[i][2]} {mat[i]}\n"
			f.write(txt)
	print("编写成功，可以直接使用了 !!")
