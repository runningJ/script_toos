import os
import shutil

def do_move(image_path,ori_label_path,tar_label_path):
	image_list=os.listdir(image_path)
	for image in image_list:
		coord_label=os.path.splitext(image)[0]+".txt"
		ori_label_file=os.path.join(ori_label_path,coord_label)
		if os.path.exists(ori_label_file):
			shutil.move(ori_label_file,tar_label_path)
		else:
			print ori_label_file


if __name__=="__main__":
	do_move("/superdb/jl/datasets/test/images",
		"/superdb/jl/datasets/train/labels",
		"/superdb/jl/datasets/test/labels")