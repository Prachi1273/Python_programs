import os

name = input("Enter name of file or folder (if name is not in current directory enter path like e.g. /home/prachi/Desktop) : ")

if not os.path.exists(name):
    print("Not Exist")
    exit()
else:
    print("Exist")