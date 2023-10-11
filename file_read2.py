import os
# Demo of FH
def main():
	print("Enter the name of file that you want to open for reading purpose : ")
	File_name = input()
	
	if os.path.exists(File_name):
		fobj=open(File_name,"r")
		if fobj:
			print("File is successfully opened in read mode")
			Line1 = fobj.readline()
			Line2 = fobj.readline()
			Line3 = fobj.readline()
			
			print("First line is : ",Line1)
			print("Second line is : ",Line2)
			print("Third line is : ",Line3)
			
			fobj.close()
			
		else:
			print("Unable to open file")	
	else:
		print("There is no such file")

if __name__ == "__main__":
	main()
