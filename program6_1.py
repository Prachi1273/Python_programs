def Display(no):
	for i in range(no):
		print("$ ",end=" ")
		print("* ",end = " ")

def main():
	no = int(input("Enter Number : "))
	
	Display(no)
	
	print()

if __name__ == "__main__":
	main()
