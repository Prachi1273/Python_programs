def Display(no):
	for digit in str(no):
		digit = no%10
		if(digit==0):
			print("There is zero")
			no = no//10
			break
		else:
			print("There is no zero")
			no = no//10
	
def main():
	no = int(input("Enter number : "))
	
	Display(no)

if __name__ == "__main__":
	main()
