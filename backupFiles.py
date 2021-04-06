import os
import shutil
source=input("Enter Source Folder Name")
destination=input("Enter The Destination Folder Name")
source=source+'/'
destination=destination+'/'
list_Of_Files=os.listdir(source)
for file in list_Of_Files:
    shutil.copy((source+file),destination)

print("Backup Taken Successfully")