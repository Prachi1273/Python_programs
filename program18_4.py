def Pattern(no):
	for i in range(1,no+1):
		print("#",end=" ")
		print(i,end=" ")
		print("*",end=" ")
		
	print()

def main():
	no = int(input("Enter number : "))
	
	Pattern(no)

if __name__ == "__main__":
	main()
