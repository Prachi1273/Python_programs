
def display(no):
	for i in range(0,no):
		for j in range(1,no+1):
			print(j,end="  ")
		print()
			
	
def main():
	print("Enter number : ")
	no = int(input())	

	ret = display(no)

if __name__ == "__main__":
	main()
