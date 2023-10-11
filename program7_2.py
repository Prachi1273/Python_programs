def Factno(no):
	fact = 1
	for i in range(1,no+1):
		fact = fact*i
	return fact

def main():
	value = int(input("Enter number : "))
	
	Ans = Factno(value)
	
	print("Factorial of ",value," is : ",Ans)

if __name__ == "__main__":
	main()
