import os 

def change(label_path,save_path,old_num,new_num):
	label_list=os.listdir(label_path)
	for each_label in label_list:
		label_file=os.path.join(label_path,each_label)
		content_list=open(label_file).read().split("\n")
		for each_content in content_list:
			if each_content=="":
				continue
			label=each_content.split()[0]
			if label==old_num:
				fw=open(os.path.join(save_path,each_label),"a")
				new_label=new_num
				bbox=each_content.split()[1:]
				bbox_str=" ".join(bbox)
				each_line=new_label+" "+bbox_str+"\n"
				fw.write(each_line)

if __name__=="__main__":
	change("/opt/jl/datasets/attribute_train/labels",
		"/opt/jl/datasets/attribute_train/filter_labels",
		"8","5")
