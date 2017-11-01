#coding:utf-8
#########################################################################
# File Name: generate_img_list.py
# Author: lei Jiang
# mail: leijiang420@163.com
# Created Time: 2016年04月07日 星期四 10时37分24秒
# Copyright Nanjing Qing So information technology
#########################################################################

import numpy as np
import os

def generateimglist(path,output):
	with open(output,'a+') as f:
		for subflod in os.listdir(path):
			subpath=os.path.join(path,subflod)
			for img in os.listdir(subpath):
				if os.path.splitext(img)[0] != "":
					imgpath=os.path.join(subpath,img)
					f.write(imgpath+'\n')
def generateimglist_file(path,output):
	with open(output,'w') as f:
		for img in os.listdir(path):
			img_path = os.path.join(path,img)
			f.write(img_path+'\n')

if __name__ == "__main__":
	generateimglist("/opt/jl/datasets/chekuan_1",
		"/opt/jl/datasets/feature_path/chekuan_1.txt")
