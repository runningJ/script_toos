import cv2
import os

'''
This function is used to crop image along height
'''
def do_crop_image(images_folder,save_folder,factor):
	if not os.path.exists(save_folder):
		os.mkdir(save_folder)
	images_list = os.listdir(images_folder)
	for image in images_list:
		if image == "":
			continue
		image_path = os.path.join(images_folder, image)
		img_mat = cv2.imread(image_path)
		img_height = img_mat.shape[0]
		if img_height == 0:
			continue
		img_width = img_mat.shape[1]
		crop_img = img_mat[int(factor*img_height):img_height,:,:]
		image_save_path = os.path.join(save_folder, image)
		cv2.imwrite(image_save_path, crop_img)

'''
This function is used to crop image along width
'''

def do_crop_image_width(image_folder,save_folder,factor):
	str_factor = str(factor).replace('.','-')
	if not os.path.exists(save_folder):
		os.mkdir(save_folder)
	images_list = os.listdir(image_folder)
	for image in images_list:
		if image == "":
			continue
		image_path = os.path.join(image_folder, image)
		img_mat = cv2.imread(image_path)
		img_width = img_mat.shape[1]
		if img_width == 0:
			crop_img = img_mat[:,0:int(factor*img_width),:]
			image_save_path = os.path.join(save_folder,image) + "_" + str_factor
			cv2.imwrite(image_save_path,crop_img)


'''
This function is used to process label images
'''
def crop_image_label(images_folder,labels_folder,factor,save_folder):

	image_save_folder = os.path.join(save_folder,"images")
	label_save_folder = os.path.join(save_folder,"labels")
	if not os.path.exists(image_save_folder):
		os.mkdir(image_save_folder)
	if not os.path.exists(label_save_folder):
		os.mkdir(label_save_folder)

	images_list = os.listdir(images_folder)
	for image in images_list:
		if image == "":
			continue
		image_path = os.path.join(images_folder, image)
		img_mat = cv2.imread(image_path)
		img_height = img_mat.shape[0]
		if img_height == 0:
			continue
		img_width = img_mat.shape[1]
		crop_img = img_mat[int(factor*img_height):img_height,:,:]
		image_save_path = os.path.join(image_save_folder, image)
		cv2.imwrite(image_save_path, crop_img)
		label_name = os.path.splitext(image)[0]+".txt"
		label_path = os.path.join(labels_folder, label_name)
		if not os.path.exists(label_path):
			continue
		fr = open(label_path,'r')
		save_label_file = os.path.join(label_save_folder, label_name)
		fw = open(save_label_file,'w')

		label_info_list = fr.read().split("\n")[:-1]
		line_size = len(label_info_list)
		if line_size > 0:
			for line in label_info_list:
				line_content=line.split()
				each_label = line_content[0]
				center_x = float(line_content[1])
				center_y = float(line_content[2])
				center_w = float(line_content[3])
				center_h = float(line_content[4])
				center_y = (center_y - factor)/(1-factor)
				center_h = center_h/(1-factor)
				trans_label = str(each_label)+" "+str(center_x)+" "+str(center_y)+" "+str(center_w)+" "+str(center_h)+"\r\n"
				fw.write(trans_label)
				
				'''
				ori_center_x = int(center_x*crop_img.shape[1])
				ori_center_y = int(center_y*crop_img.shape[0])
				ori_center_w = int(center_w*crop_img.shape[1])
				ori_center_h = int(center_h*crop_img.shape[0])

				half_w = int(0.5*ori_center_w)
				half_h = int(0.5*ori_center_h)

				cv2.rectangle(crop_img,(ori_center_x - half_w, ori_center_y-half_h),
					(ori_center_x + half_w, ori_center_y +half_h),
						(0,255,0),2)
				'''


if __name__ == "__main__":
	
	do_crop_image("/opt/jl/datasets/car_plate/plate_2017_10_10_no",
		"/opt/jl/datasets/car_plate/plate_2017_10_10_no_factor",0.5)
	'''
	crop_image_label("/opt/jl/datasets/car_plate/plate_2017_10_1",
		"/opt/jl/datasets/car_plate/change_labels",0.5,
		"/opt/jl/datasets/car_plate/crop")
	'''
