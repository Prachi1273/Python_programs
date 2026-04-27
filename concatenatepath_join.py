import os 

filename = 'f1.txt'
foldername = 'sample'

os.path.join(foldername,filename)

print(os.path.join(foldername,filename))

'''
os.path.join() is used to safely construct the full/complete path by combining folder names and filenames, regardless of the operating system.

🔧 Think of it as:
✔️ It does not create the file/folder,
✔️ It does not check existence,
✔️ It only builds the correct path string, which you can then use for creating, moving, or accessing files.
'''
