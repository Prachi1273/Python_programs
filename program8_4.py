def Display(no):		
	if(no<0):
		no = -no
	fact = 1
	for i in range(1,no+1):
		if(i%2!=0):
			fact = fact*i
	print(fact)
	
def main():
	value = int(input("Enter number : "))
	
	Display(value)

if __name__ == "__main__":
	main()
