def Display(no):
	rev = 0
	while(no>0):
		digit = no%10
		rev = rev*10+digit
		no=no//10
	print(rev)
	
def main():
	no = int(input("Enter number : "))
	
	Display(no)

if __name__ == "__main__":
	main()
