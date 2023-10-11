def Pattern(no):
	for i in range(no,0,-1):
		print(i,end=" ")
		print("#",end=" ")
		
	print()

def main():
	no = int(input("Enter number : "))
	
	Pattern(no)

if __name__ == "__main__":
	main()
