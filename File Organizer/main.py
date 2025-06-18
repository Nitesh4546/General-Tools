import os
import sys
import shutil
from extensions import extn, doc, pic, audi, video, archive
#different extensions for the same type of file



#checking if the user has provided a path
if len(sys.argv)==1:
    sys.exit("Please provide a folder path as an argument.")
#checking if the user has provided help argument
if sys.argv[1] in ['-h','--help']:
    print("Usage: python AutoOrganizer.py <path_to_directory>")
    print("This script organizes files in the specified directory into subdirectories based on their file types.")
    sys.exit(0)
elif not os.path.isdir(sys.argv[1]):
    sys.exit("The provided path is not a directory.")
path = sys.argv[1].strip()

#checking the validity of the path entered
if not os.path.exists(path):
    sys.exit("Invalid path.")

#Changing the dir.
os.chdir(path)


types = set()#stores unique extensions avaliable in a dir.
files = []#stores all the files

#looping over each file
for item in os.listdir():
    
    #checking if item is a file or folder 
    if os.path.isfile(item):
        
        #adding the files to list to use it later
        files.append(item)
        
        #sepatrating the ext fromt the filename
        ext = item.split(".")[-1]
        
        #checks for the extensions in the predefined lists
        if ext in doc:
            types.add("doc")
        elif ext in pic:
            types.add("pic")
        elif ext in archive:
            types.add("archive")
        elif ext in audi:
            types.add("audio")
        elif ext in video:
            types.add("video")

        else:
            #checks for the extenions in the dic use them as keys
            try:
                types.add(extn[ext])
            except KeyError:
                types.add("Other Files")

#creating folder for the types of files
for i in types:
    os.mkdir(i, exist_ok=True)

for file in files:
    ext = file.split(".")[-1].lower()
    #checks for the extensions and move them to their folder
    if ext in doc:
        shutil.move(file,"doc")
    elif ext in pic:
        shutil.move(file,"pic")
    elif ext in archive:
        shutil.move(file,"archive")
    elif ext in audi:
        shutil.move(file,"audio")
    elif ext in video:
        shutil.move(file,"video")
    else:
        #checks for the extenions in the dic use them as keys and move them to their folder
        try:
            shutil.move(file,extn[ext])
        except KeyError:
            shutil.move(file,"Other Files")
print("The files are organized.")