from shutil import move
import os
import sys
c = 0

for file in os.listdir("E:\Python\Trial"):
    y = os.path.splitext(file)[1]
    print (y)
ip = input("Choose a file extension to move from the list -> ")

src_dir = 'Trial'
target_dir = 'jaadu'


for files in os.listdir(src_dir):
       
    dst = os.path.join(target_dir, files)

    src = os.path.join(src_dir, files)

    if files.endswith(ip):
        move(src,dst)
        c+=1
       
print (f'total files moved: {c}')
