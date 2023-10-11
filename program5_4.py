def chk(no1,no2,no3):
	if(no1==0):
		no1 = 1
	if(no2==0):
		no2 = 1
	if(no3==0):
		no3 = 1
	
	Mult = no1*no2*no3
	return Mult

def main():
	no1 = int(input("Enter First Number : "))
	no2 = int(input("Enter Second Number : "))
	no3 = int(input("Enter Third Number : "))
	
	Ans = chk(no1,no2,no3)
	
	print("Multiplication of ",no1,",",no2,",",no3," is : ",Ans)

if __name__ == "__main__":
	main()
