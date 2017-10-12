import os

def filter(train_path):
	train_list=open(train_path,'r').read().split("\n")
	i=0
	for train_file in train_list:
		if train_file=="":
			continue
		label_file=train_file.replace('images','labels')
		label_file=label_file.replace('jpg','txt')
		label_list=open(label_file,'r').read().split('\n')
		i=i+1
		if label_list[0]=="":
			print '----------------'
			print label_file
	print i

if __name__=="__main__":
	filter('/opt/jl/datasets/boat/train.txt')