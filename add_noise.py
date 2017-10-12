import cv
import os
import os.path
import sys
import shutil

def addGaussianNoise(image_path,save_path):
	img = cv.LoadImage(image_path)
	noise = cv.CreateImage(cv.GetSize(img),img.depth,img.nChannels)
	cv.SetZero(noise)
	rng = cv.RNG(-1)
	cv.RandArr(rng,noise,cv.CV_RAND_NORMAL,cv.ScalarAll(0),cv.ScalarAll(25))
	cv.Add(img,noise,img)
	tempName = os.path.splitext(os.path.basename(image_path))[0]+"_noised.jpg"
	save_image=os.path.join(save_path,tempName)
	cv.SaveImage(save_image,img)

def copy_labels(label_file,ori_path,save_path):
	save_file=os.path.join(save_path,label_file+"_noised.txt")
	ori_file=os.path.join(ori_path,label_file+'.txt')
	shutil.copy(ori_file,save_file)

def process_folder(image_folder_path,label_path,save_image_folder,save_label_folder):
	image_list=os.listdir(image_folder_path)
	total_num=len(image_list)
	print "total has %d images"%total_num
	idx=0;
	for img_file in image_list:
		if idx%1000==0:
			print "process %d/%d"%(idx,total_num)
		image_path=os.path.join(image_folder_path,img_file)
		addGaussianNoise(image_path,save_image_folder)
		file_base=os.path.splitext(img_file)[0]
		copy_labels(file_base,label_path,save_label_folder)
		idx=idx+1


if __name__ == "__main__":
	process_folder('/opt/jl/datasets/car_plate/plate_train/images',
		'/opt/jl/datasets/car_plate/plate_train/labels',
		'/opt/jl/datasets/car_plate/aug_plate_train/images',
		'/opt/jl/datasets/car_plate/aug_plate_train/labels')
