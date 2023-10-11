import time
from sys import *
import os

def DirectoryTravel(DirName,name):
	print("We are going to scan the Directory : ",DirName)
	
	flag = os.path.isabs(DirName)
	
	if flag==False:
		DirName = os.path.abspath(DirName)
		
	exist=os.path.isdir(DirName)
		
	if exist:
		for foldername,subfoldername,filename in os.walk(DirName):	
			for fname in filename:		
				if(fname==name):
					print("File is present in the directory with name ",fname)
					return
	else :
		print("Invalid path")

def main():
	print("---------------Automation Script-----------")
	
	print("Automation script : ",argv[0])
	
	
	
	if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
		print("This automation script is used to perform file automations ")
		exit()

	elif(argv[1]=="-u" or argv[1]=="-U"):		#flag for displaying usage of script
		print("Usage : name_Of_Script First_argument Second_Argument ")
		print("Example : Demo.py Prachi(Directory_Name) demo.txt(filename)")
		exit()
	
	if(len(argv)!=3):
		print("Invalid no. of argumaents ")
		exit()
		
	else:
		starttime=time.time()
		DirectoryTravel(argv[1],argv[2])
		endtime=time.time()
		
		print("The Script took time to execute is : ",endtime-starttime)

if __name__ == "__main__":
	main()
