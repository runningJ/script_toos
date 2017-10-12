import os
import cv2

def change(bbox,width,height):
	dw = 1./width
	dh = 1./height
	c_x=bbox[0]
	c_y=bbox[1]
	w=bbox[2]
	h=bbox[3]
	ori_c_x=c_x/dw
	ori_c_y=c_y/dh
	ori_w=w/dw
	ori_h=h/dh
	xmin=int(ori_c_x-ori_w/2)
	ymin=int(ori_c_y-ori_h/2)
	xmax=int(ori_c_x+ori_w/2)
	ymax=int(ori_c_y+ori_h/2)
	return [ymin,xmin,ymax,xmax]


def do_trans(image_folder,label_folder,save_label):

	image_list=os.listdir(image_folder)
	for image in image_list:
		image_path=os.path.join(image_folder,image)
		img=cv2.imread(image_path)
		image_width=img.shape[1]
		image_height=img.shape[0]
		image_base_name=os.path.splitext(image)[0]
		ori_label_file=os.path.join(label_folder,image_base_name+'.txt')
		save_label_file=os.path.join(save_label,image+'.txt')
		fr=open(ori_label_file,'r')
		fw=open(save_label_file,'w')
		line_list=fr.read().split("\n")
		line_size=len(line_list)-1
		first_line=str(line_size)+"\r\n"
		fw.write(first_line)
		if line_size>0:
			for line in line_list:
				if line=="":
					continue
				line_content=line.split()
				each_label=line_content[0]
				center_x=float(line_content[1])
				center_y=float(line_content[2])
				center_w=float(line_content[3])
				center_h=float(line_content[4])
				trans_bbox=change([center_x,center_y,center_w,center_h],image_width,image_height)
				label_record=str(trans_bbox[0])+" "+str(trans_bbox[1])+" "+str(trans_bbox[2])+" "+str(trans_bbox[3])+"\r\n"+each_label+"\r\n"+'0'+'\r\n'
				fw.write(label_record)





if __name__=="__main__":
	do_trans("/opt/jl/datasets/attribute_train/images",
		"/opt/jl/datasets/attribute_train/labels",
		"/opt/jl/datasets/attribute_train/save_labels")
