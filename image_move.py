import shutil
import os
f = open("taihuang.txt")

path = './filter_region/'
new_path = './moss_yellow/'
all_lines = f.readlines()
for line in all_lines:
    line = line.strip('\n')
    old_name = path + line
    new_name = new_path + line
    print(new_name)
    if os.path.exists(old_name):
        shutil.move(old_name, new_name)