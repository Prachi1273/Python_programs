
def NFactAdd(no):
	add = 0
	add1 = 0
	for i in range(1,no):
		if(no%i!=0):
			add=add+i
		elif(no%i==0):
			add1 = add1+i
	return add,add1

def main():
	iValue = int(input("Enter one number : "))
	
	Ans = NFactAdd(iValue)
	
	print("Addition of Non Factors : ",Ans[0])
	print("Addition of Factors : ",Ans[1])
	print("Diffrence between Summation of Factors and Non-Factors is : ",Ans[1]-Ans[0])

if __name__  == "__main__":
	main()
