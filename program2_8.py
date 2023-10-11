def Display(no):
	for i in range(1,no+1):
		for j in range(1,no+1):
			if(j<=i):
				print(j,end=" ")
		print()

def main():
	print("Enter number : ")
	no = int(input())
	
	Display(no)

if __name__ == "__main__":
	main()
