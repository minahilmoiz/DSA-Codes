import os

drive = "G:\\"
drv = os.scandir(drive)
for dir in drv:
    if dir.is_dir:
        print (dir.name)
        print ('======================')
        obj = dir.path
        os.scandir(obj)
        for file in os.scandir(obj):
            if file.is_file:
                print (file.name)
