import Prachi

def main():
	Value1 = int(input("Enter First number : "))
	Value2 = int(input("Enter second number : "))
	
	Result = 0
	
	Result = Prachi.Addition(Value1,Value2)
	print("Addition is : ",Result)
	
	Result = Prachi.Subtraction(Value1,Value2)
	print("Subtraction is : ",Result)
	
	Result = Prachi.Multiplication(Value1,Value2)
	print("Multiplication is : ",Result)
	
	Result = Prachi.Division(Value1,Value2)
	print("Division is : ",Result)

if __name__ == "__main__":
	main()

