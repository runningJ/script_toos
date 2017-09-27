from data_augmentor import Data_augmentor
import shutil
import os

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
	process_folder('/opt/jl/datasets/car_plate/plate_train/images',
		'/opt/jl/datasets/car_plate/plate_train/labels',
		"/opt/jl/datasets/car_plate/aug_plate_train/images",
		"/opt/jl/datasets/car_plate/aug_plate_train/labels")