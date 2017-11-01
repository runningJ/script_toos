import os

def file_in_folder(folder_path):
	folder_name=os.path.basename(folder_path)
	file_list=os.listdir(folder_path)
	for i,file in enumerate(file_list):
		file_name,file_ext=os.path.splitext(file)
		new_name=folder_name+"_"+str(i)+file_ext
		os.rename(os.path.join(folder_path,file),
			os.path.join(folder_path,new_name))

def rename_file(folder_path, name):
	file_list = os.listdir(folder_path)
	for file in file_list:
		file_base,file_ext = os.path.splitext(file)
		if file_base != "ssss":
			new_name = name+file_ext
			os.rename(os.path.join(folder_path,file),
				os.path.join(folder_path,new_name))

def rename(folder_path):
	subfolder_list = os.listdir(folder_path)
	for subfolder in subfolder_list:
		file_in_folder(os.path.join(folder_path,subfolder))

def rename_folder(folder_path, name):
	subfolder_list = os.listdir(folder_path)
	for subfolder in subfolder_list:
		rename_file(os.path.join(folder_path,subfolder),name)


if __name__=="__main__":
	rename("/opt/jl/generate-plate/images/results")
