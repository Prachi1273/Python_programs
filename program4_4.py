
def NFactAdd(no):
	add = 0
	for i in range(1,no):
		if(no%i!=0):
			add=add+i
	return add

def main():
	iValue = int(input("Enter one number : "))
	
	Ans = NFactAdd(iValue)
	
	print("Addition of Non Factors : ",Ans)

if __name__  == "__main__":
	main()
