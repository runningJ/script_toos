import os
import random
import shutil

def extract_from_folder(folder_path,number,save_path):
	images_list=os.listdir(folder_path)
	extract_list=random.sample(images_list,number)
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	for image in extract_list:
		image_path=os.path.join(folder_path,image)
		shutil.move(image_path,save_path)


if __name__=="__main__":
	extract_from_folder("/opt/jl/datasets/video_train/images",1000,
		"/opt/jl/datasets/video_train/val")