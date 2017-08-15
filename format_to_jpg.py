import cv2
import os

def change_format(image_path):
	images_list=os.listdir(image_path)
	for image in images_list:
		img=cv2.imread(os.path.join(image_path,image))
		new_image=os.path.splitext(image)[0]+".jpg"
		save_path=os.path.join(image_path,new_image)
		cv2.imwrite(save_path,img)


if __name__=="__main__":
	change_format("/superdb/jl/datasets/car/car2017_4_8")