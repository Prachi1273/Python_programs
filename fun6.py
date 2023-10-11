
# function accept multiple parameter and return multiple parameter
def Exellent(value1,value2):
	Add = value1 + value2
	sub = value1 - value2
	mult = value1 * value2
	
	return Add,sub,mult
	
def main():
	ret = Exellent(11,6)
	print("Addition is : ",ret[0])
	print("Subtraction is : ",ret[1])
	print("Multiplication is : ",ret[2])		
	
if __name__ == "__main__":
	main()
