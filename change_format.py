import cv2
import os

def change_format(images_folder,out_put_folder):
	image_list=os.listdir(images_folder)
	for image in image_list:
		image_path=os.path.join(images_folder,image)
		img=cv2.imread(image_path)
		image_name=os.path.splitext(image)[0]
		save_name=image_name+".jpg"
		if not os.path.exists(out_put_folder):
			os.mkdir(out_put_folder)
		save_path=os.path.join(out_put_folder,save_name)
		cv2.imwrite(save_path,img)

if __name__=="__main__":
	change_format("/opt/jl/datasets/car_plate/plate_train/two_line_plate",
		'/opt/jl/datasets/car_plate/plate_train/change_format')
