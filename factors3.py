def chkfactor:
	for i in range(1,No,1):
		if(No % i == 0):
			print(i)
			
def main:
	No = int(input("Enter no. : "))
	chkfactor(No)
	
if __name__ == "__name__":
	main()
