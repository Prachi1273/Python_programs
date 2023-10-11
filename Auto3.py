from sys import *
from Arithmetic import *

def main():
	print("---------------Automation Script-----------")
	
	print("Automation script : ",argv[0])
	
	if(len(argv)==2):
		if(argv[1]=="-h" or argv[1]=="-H"):         #flag for displaying help
			print("This automation script is used to perform addition of two numbers ")
			exit()
	
		elif(argv[1]=="-u" or argv[1]=="-U"):		#flag for displaying usage of script
			print("Usage : name_Of_Script First_argumaent Second_argumaent")
			print("Example : Demo.py 11 10")
			exit()
			
		else:
			print("There is no such option to handle")
		
	if(len(argv)!=3):
		print("Invalid no. of argumaents ")
		exit()
	else:
		Ret=Addition(int(argv[1]),int(argv[2]))
		print("Addition is : ",Ret)

if __name__ == "__main__":
	main()
