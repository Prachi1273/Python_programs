def Display(no):		
	if(no<0):
		no = -no
	fact = 1
	fact1 = 1
	for i in range(1,no+1):
		if(i%2!=0):
			fact = fact*i
		elif(i%2==0):
			fact1 = fact1*i
	print("Odd Factorial",fact)
	print("Even Factorial",fact1)
	return diff(fact,fact1)
	
def diff(fact,fact1):
	diff=fact1-fact
	print(diff)
	
def main():
	value = int(input("Enter number : "))
	
	Display(value)

if __name__ == "__main__":
	main()
