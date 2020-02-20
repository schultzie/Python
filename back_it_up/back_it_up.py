# Written by Greg Schultz

import os
import sys
import getpass
import shutil

orig_stdout = sys.stdout
f = open('transfer_log.txt', 'w')
sys.stdout = f

name = getpass.getuser()
print("User is " + name)

idrive = f'//share/drive/location/{name}'
if not os.path.exists(idrive):
    os.makedirs(idrive)
print('Backup Folder Created')

user_folder = f'c:/Users/{name}'
folders = ['/Documents', '/Favorites', '/Pictures', '/Desktop']

full_folder = []

for i in folders:
    full_folder.append(user_folder + i)
print('Folder to copy Identified')


def get_files(file_name):
    for src_dir, dirs, files in os.walk(file_name):
        dst_dir = src_dir.replace(file_name, idrive, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
            break
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)


for i in full_folder:
    get_files(i)
    print(f'Files in {i} have been copied')

shutil.copy(f'C:/Users/{name}/AppData/Local/Google/Chrome/User Data/Default/Bookmarks', idrive)

print('Done moving files to I drive')

sys.stdout = orig_stdout
f.close()
