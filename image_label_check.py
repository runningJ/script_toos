import os
import shutil

def check(image_path,label_path):
	'''
	for ours labels
	'''
	image_list=os.listdir(image_path)
	for image in image_list:
		coord_label=image+".txt"
		absolute_path=os.path.join(label_path,coord_label)
		if os.path.exists(absolute_path):
			continue
		else:
			os.system("rm "+os.path.join(image_path,image))
	label_list=os.listdir(label_path)
	for label in label_list:
		coord_image=os.path.splitext(label)[0]
		absolute_path=os.path.join(image_path,coord_image)
		if os.path.exists(absolute_path):
			continue
		else:
			os.system("rm "+os.path.join(label_path,label))


def check_version(image_path,label_path):
	'''
	for yolo labels
	'''
	image_list=os.listdir(image_path)
	for image in image_list:
		coord_label=os.path.splitext(image)[0]+".txt"
		absolute_path=os.path.join(label_path,coord_label)
		if os.path.exists(absolute_path):
			continue
		else:
			print absolute_path
			os.system("rm "+os.path.join(image_path,image))
			
	label_list=os.listdir(label_path)
	for label in label_list:
		coord_image=os.path.splitext(label)[0]+".jpg"
		absolute_path=os.path.join(image_path,coord_image)
		if os.path.exists(absolute_path):
			continue
		else:
			os.system("rm "+os.path.join(label_path,label))
			print absolute_path

if __name__=="__main__":
	check("/opt/jl/datasets/car_plate/plate_train/images",
		"/opt/jl/datasets/car_plate/plate_train/labels")
