from sys import *
import os

def DirectoryTravel(DirName):
	print("We are going to scan the Directory : ",DirName)
	
	for foldername,subfoldername,filename in os.walk(DirName):
		print("Current Directory Name : ",foldername)
		
		for subname in subfoldername:
			print("Subfolder name is : ",subname)
		
		for fname in filename:
			print(fname)

def main():
	print("---------------Automation Script-----------")
	
	print("Automation script : ",argv[0])
	
	if(len(argv)!=2):
		print("Invalid no. of argumaents ")
		exit()
	
	if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
		print("This automation script is used to perform file automations ")
		exit()

	elif(argv[1]=="-u" or argv[1]=="-U"):		#flag for displaying usage of script
		print("Usage : name_Of_Script First_argument ")
		print("Example : Demo.py Prachi(Directory_Name)")
		exit()
		
	else:
		DirectoryTravel(argv[1])

if __name__ == "__main__":
	main()
