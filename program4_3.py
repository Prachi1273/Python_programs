
def FactMult(no):
	mult = 1
	for i in range(no,1,-1):
		if(no%i!=0):
			print(i)

def main():
	iValue = int(input("Enter one number : "))
	
	FactMult(iValue)

if __name__  == "__main__":
	main()
