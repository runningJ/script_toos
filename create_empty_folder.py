import os

def do_create_empty_folder(folder_path):
	for i in range(1,98):
		folder_name = str(i + 23078)
		sub_folder_path = os.path.join(folder_path,folder_name)
		os.mkdir(sub_folder_path)

if __name__ == "__main__":
	do_create_empty_folder("/opt/jl/datasets/empty")