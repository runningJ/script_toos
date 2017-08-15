import os
import cv2

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def label_process(image_path,label_path,save_path):
	labeltxt_list=os.listdir(label_path)
	for label_txt in labeltxt_list:
		if label_txt=="":
			continue
		image_name=os.path.splitext(label_txt)[0]
		image_name=os.path.splitext(image_name)[0]+".jpg"
		img=cv2.imread(os.path.join(image_path,image_name))
		size=[img.shape[1],img.shape[0]]
		label_txt_path=os.path.join(label_path,label_txt)
		fo=open(label_txt_path,'r')
		content_list=fo.read().split("\r\n")
		label_num=int(content_list[0])
		new_label_file=os.path.splitext(image_name)[0]+".txt"
		fw=open(os.path.join(save_path,new_label_file),'a')
		for i in xrange(label_num):
			bbox_str=content_list[i*3+1].split()
			label_str=content_list[i*3+2]
			ymin=float(bbox_str[0])
			xmin=float(bbox_str[1])
			ymax=float(bbox_str[2])
			xmax=float(bbox_str[3])
			bbox_norm=convert(size,[xmin,xmax,ymin,ymax])
			eachline=label_str+" "+str(bbox_norm[0])+" "+str(bbox_norm[1])+" "+str(bbox_norm[2])+" "+str(bbox_norm[3])+'\n'
			fw.write(eachline)


if __name__=="__main__":
	label_process("/opt/jl/datasets/car_plate/plate-2017-7-18/images",
		"/opt/jl/datasets/car_plate/plate-2017-7-18/labels",
		"/opt/jl/datasets/car_plate/plate-2017-7-18/change_labels")
