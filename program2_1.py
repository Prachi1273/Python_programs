import Arithmetic

def main():
	print("Enter first number : ")
	no1 = int(input())
	
	print("Enter second number : ")
	no2 = int(input())
	
	ret = Arithmetic.Add(no1,no2)
	print("Addition is : ",ret)
	
	ret = Arithmetic.Sub(no1,no2)
	print("Subtraction is : ",ret)

	ret = Arithmetic.Mult(no1,no2)
	print("Multiplication is : ",ret)

	ret = Arithmetic.Div(no1,no2)
	print("Division is : ",ret)


if __name__ == "__main__":
	main()
