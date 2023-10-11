
def Addition(No1,No2):
	Result = 0
	Result = No1 + No2
	return Result


def main():
	Value1 = int(input("Enter First number : "))

	Value2 = int(input("Enter second number : "))

	Answer = 0
	Answer = Addition(Value1,Value2)

	print("Addition is : ",Answer)

if __name__ == "__main__":  	#starter
	main()
	
#if there are 2 underscores at starting && ending of variable is called as special variable
