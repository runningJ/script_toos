import os
import shutil

def extract(images_path,image_save_path,label_save_path):
	images_list=os.listdir(images_path)
	for image in images_list:
		if image=="":
			continue
		if 'set' in image:
			image_file=os.path.join(images_path,image)
			label_file=image_file.replace("images","labels")
			label_file=label_file.replace("jpg","txt")
			shutil.copy(image_file,image_save_path)
			shutil.copy(label_file,label_save_path)



if __name__=="__main__":
	extract("/superdb/jl/datasets/video_train/images",
		"/superdb/jl/datasets/person_train/images",
		"/superdb/jl/datasets/person_train/labels")