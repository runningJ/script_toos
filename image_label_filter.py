import os
import shutil

def filter(image_path,label_path,save_path):
	image_list=os.listdir(image_path)
	for image in image_list:
		image_name=os.path.splitext(image)[0]
		label_name=image_name+'.jpg.txt'
		label_file=os.path.join(label_path,label_name)
		if not os.path.exists(label_file):
			print label_file
		else:
			shutil.copy(label_file,save_path)


if __name__=="__main__":
	filter("/superdb/jl/datasets/boat/images",
		"/superdb/jl/datasets/boat/labels",
		"/superdb/jl/datasets/boat/clean_labels")
