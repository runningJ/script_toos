import os

def file_in_folder(folder_path):
	folder_name=os.path.basename(folder_path)
	file_list=os.listdir(folder_path)
	for i,file in enumerate(file_list):
		file_name,file_ext=os.path.splitext(file)
		new_name=folder_name+"_"+str(i)+file_ext
		os.rename(os.path.join(folder_path,file),
			os.path.join(folder_path,new_name))

def rename(folder_path):
	subfolder_list=os.listdir(folder_path)
	for subfolder in subfolder_list:
		file_in_folder(os.paht.join(folder_path,subfolder))


if __name__=="__main__":
	file_in_folder("/cache/datasets/chewei/172")
