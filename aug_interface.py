from data_augmentor import Data_augmentor
import shutil
import os
from add_noise import addGaussianNoise

da=Data_augmentor()
suffix="bright"

def copy_labels(label_file,ori_path,save_path):
	save_file=os.path.join(save_path,label_file+"_"+suffix+".txt")
	ori_file=os.path.join(ori_path,label_file+'.txt')
	#print save_file
	shutil.copy(ori_file,save_file)

def do_augment(image_path,factor,save_path):
	res,method=da.change_brightness(image_path,factor)
	image_name=os.path.splitext(os.path.basename(image_path))[0]+"_"+suffix+".jpg"
	save_name=os.path.join(save_path,image_name)
	#print save_name
	res.save(save_name)

def do_augment_folder(folder_path, factor, save_path):
	str_factor = str(factor).replace('.','-')
	image_list = os.listdir(folder_path)
	for image_name in image_list:
		image_file = os.path.join(folder_path, image_name)
		if os.path.exists(image_file):
			res, method = da.change_contrast(image_file,factor)
			save_name = os.path.splitext(image_name)[0] + "_"+method +str_factor+".jpg"
			if not os.path.exists(save_path):
				os.makedirs(save_path)
			save_file = os.path.join(save_path, save_name)
			res.save(save_file)
		else:
			print image_file

def do_nosie_folder(folder_path, save_path):
	image_list = os.listdir(folder_path)
	for image_name in image_list:
		image_file = os.path.join(folder_path,image_name)
		if os.path.exists(image_file):
			if not os.path.exists(save_path):
				os.makedirs(save_path)
			addGaussianNoise(image_file,save_path)
		else:
			print image_file

def process_train(folder_path, process_name, factor):

	folder_list = os.listdir(folder_path)
	for i, each_folder in enumerate(folder_list):
		print "do %s %d of %d %s %f" %(each_folder,i,len(folder_list),process_name,factor)
		each_folder_path = os.path.join(folder_path, each_folder)
		save_folder = os.path.split(folder_path)[0]+"/"+process_name
		save_folder_path = os.path.join(save_folder, each_folder)
		do_nosie_folder(each_folder_path,save_folder_path)



def process_folder(image_folder_path,label_path,image_save_folder,label_save_path):
	image_list=os.listdir(image_folder_path)
	total_num=len(image_list)
	print "total has %d images"%total_num
	idx=0;
	for img_file in image_list:
		if idx%1000==0:
			print "process %d/%d"%(idx,total_num)
		image_path=os.path.join(image_folder_path,img_file)
		do_augment(image_path,0.5,image_save_folder)
		file_base=os.path.splitext(img_file)[0]
		copy_labels(file_base,label_path,label_save_path)
		idx=idx+1

if __name__=="__main__":
	process_train("/opt/datasets/same_car_image/ori_image","aug_gaussian_noise",0.5)
	'''
	process_folder('/opt/jl/datasets/car_plate/plate_train/images',
		'/opt/jl/datasets/car_plate/plate_train/labels',
		"/opt/jl/datasets/car_plate/aug_plate_train/images",
		"/opt/jl/datasets/car_plate/aug_plate_train/labels")
	'''
