def Display(no):
	while(no>0):
		digit = no%10
		no=no//10
		print(digit)
	
def main():
	no = int(input("Enter number : "))
	
	Display(no)

if __name__ == "__main__":
	main()
