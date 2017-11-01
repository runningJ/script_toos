import os
import random

def generate(images_path,save_path,number):
	images_list=os.listdir(images_path)
	random.shuffle(images_list)
	extract_list=random.sample(images_list,number)
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	train_file=os.path.join(save_path,'train.txt')
	val_file=os.path.join(save_path,'val.txt')
	ftrain=open(train_file,'w')
	fval=open(val_file,'w')
	train_list=list(set(images_list).difference(set(extract_list)))
	print "val image numbers:%i"%len(extract_list)
	print "tarin image numbers:%i"%len(train_list)
	for train_image in train_list:
		each_line=os.path.join(images_path,train_image)+'\n'
		ftrain.write(each_line)
	for val_image in extract_list:
		each_line=os.path.join(images_path,val_image)+'\n'
		fval.write(each_line)

def generate_train(images_path,save_path):
	images_list=os.listdir(images_path)
	random.shuffle(images_list)
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	train_file=os.path.join(save_path,'train.txt')
	ftrain=open(train_file,'w')
	train_list=images_list
	print "tarin image numbers:%i"%len(train_list)
	for train_image in train_list:
		each_line=os.path.join(images_path,train_image)+'\n'
		ftrain.write(each_line)

def generate_val(images_path,save_path):
	images_list=os.listdir(images_path)
	random.shuffle(images_list)
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	train_file=os.path.join(save_path,'val.txt')
	ftrain=open(train_file,'w')
	train_list=images_list
	print "val image numbers:%i"%len(train_list)
	for train_image in train_list:
		each_line=os.path.join(images_path,train_image)+'\n'
		ftrain.write(each_line)

if __name__=="__main__":
	#generate_val("/superdb/jl/datasets/test/images","/superdb/jl/datasets/test")
	generate_train("/opt/jl/datasets/new_attribute/train/images",
		"/opt/jl/datasets/new_attribute/train")
