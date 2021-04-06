import os
import shutil
path=input("Enter The Name Of The Directory To Be Sorted")
list_Of_Files=os.listdir(path)
for file in list_Of_Files:
    Name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext == '':
        continue

    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

print("File Sorted Successfully") 