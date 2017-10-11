import os

def do_create_label(image_path,save_path):
	if not os.path.exists(image_path):
		print "image folder is not exists"
		exit(0)
	if not os.path.exists(save_path):
		os.mkdir(save_path)
	image_list = os.listdir(image_path)
	for image_file in image_list:
		image_name = os.path.splitext(image_file)[0]
		label_name = image_name +".txt"
		save_label_path = os.path.join(save_path,label_name)
		f = open(save_label_path,"w")
		


if __name__=="__main__":
	do_create_label("/opt/jl/datasets/car_plate/plate_2017_10_10_no",
		"/opt/jl/datasets/car_plate/labels")
