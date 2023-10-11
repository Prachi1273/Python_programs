def Display(no):
	icnt = 0
	for digit in str(no):
		digit = no%10
		if(digit==2):
			icnt+=1
		no = no//10
	return icnt
	
def main():
	no = int(input("Enter number : "))
	
	Ans = Display(no)
	print("Number of 2 are : ",Ans)

if __name__ == "__main__":
	main()
