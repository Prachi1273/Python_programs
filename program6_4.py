def Display(no):
	for i in range(1,no+1):
		if(i%2!=0):
			print(i,end=" ")

def main():
	no = int(input("Enter Number : "))
	
	Display(no)
	
	print()
	
if __name__ == "__main__":
	main()
