
def FactMult(no):
	mult = 1
	for i in range(1,no):
		if(no%i==0):
			mult = mult*i
	return mult

def main():
	iValue = int(input("Enter one number : "))
	
	Ans = FactMult(iValue)
	
	print("Multiplication of factors is : ",Ans)
	

if __name__  == "__main__":
	main()
