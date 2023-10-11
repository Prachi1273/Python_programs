
# function accept multiple parameter and return multiple parameter
def Exellent(value1,value2):
	Add = value1 + value2
	sub = value1 - value2
	mult = value1 * value2
	
	return Add,sub,mult
	
def main():
	ret1,ret2,ret3 = Exellent(11,6)
	print("Addition is : ",ret1)
	print("Subtraction is : ",ret2)
	print("Multiplication is : ",ret3)		
	
if __name__ == "__main__":
	main()
