import os

dir_path = r'C:\Users\MHT\Desktop'

all_files = os.listdir(dir_path)
only_txt_files = filter(lambda f_path: f_path.endswith(".txt"), all_files)
new_file = open('files_merged.txt', 'w')
for txt_file in only_txt_files:
    new_file.write(open(os.path.join(dir_path, txt_file)).read())

