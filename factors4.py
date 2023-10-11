
def chkfactor(No):
	i=1
	while(i<No):
		if(No % i == 0):
			print(i)
		i = i+1
			
def main():
	No = int(input("Enter no. : "))
	chkfactor(No)
	
if __name__ == "__main__":
	main()
