import os

no = int(input("Enter no. of times to chk : "))

for i in range(no):
	name = input("Enter name of file/folder : ")
	
	if os.path.isdir(name):
		print("Dir")
	elif os.path.isfile(name):
		print("File")
	else:
		print("other")
