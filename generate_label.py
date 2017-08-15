import os

def generate_label(image_floder,save_file):
	image_list=os.listdir(image_floder)
	with open(save_file,'w') as f:
		for image in image_list:
			image_path=os.path.join(image_floder,image)
			each_line=image_path+'\n'
			f.write(each_line)

if __name__=="__main__":
	generate_label("/opt/jl/datasets/video_train/val","/opt/jl/datasets/video_train/val.txt")