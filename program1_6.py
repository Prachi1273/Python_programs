def display(no):
	for i in range(0,no):
		print("*  ",end = "")

def main():
	print("Enter number : ")
	no = int(input())
	
	display(no)

if __name__ == "__main__":
	main()
