def Display(no):
	for i in range(1,6):
		print(no*i,end=" ")

def main():
	no = int(input("Enter Number : "))
	
	Display(no)
	
	print()
	
if __name__ == "__main__":
	main()
