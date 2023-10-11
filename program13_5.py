def EvenOddCount(no):
	icnt = 0
	i=0
	dig = 0
	while(no>0):
		dig = no % 10
		if(dig %2 == 0):
			icnt = icnt+dig
		elif(dig == 0):
			icnt = icnt+0
		else:
			i = i+dig
		no = int(no/10)
	return Diff(icnt,i)

def Diff(icnt,i):
	print("Summation of Even Digits : ",icnt)
	print("Summation of Odd Digits : ",i)
	print("Diffrence between Summation of Even & Odd Digits is : ",(icnt-i))

def main():
	no = int(input("Enter a Number : "))
	
	EvenOddCount(no)

if __name__ == "__main__":
	main()
	
