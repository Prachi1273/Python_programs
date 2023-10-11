import os

def main():
	print("Enter the name of file that you want to open for Writing purpose : ")
	File_name = input()
	
	if os.path.exists(File_name):
		fobj=open(File_name,"a")
		if fobj:
			print("File is successfully opened in append mode")
			print("Enter the data that you want to write in the file : ")
			Data = input()
			fobj.write(Data)
			
			fobj.close()
			
		else:
			print("Unable to open file")	
	else:
		print("There is no such file")

if __name__ == "__main__":
	main()
