import os 

mypath= '/home/prachi/Desktop/ppa/c/hello.c'

#both real,abspath gives absolute path

#Resolve symlinks to actual file
realp = os.path.realpath('makedir.py')
print(realp)

absp = os.path.abspath('/Automation/listfilefolder.py')
print(absp)

normp = os.path.normpath(mypath)
print(normp)

realp = os.path.relpath(mypath)
print(realp)
