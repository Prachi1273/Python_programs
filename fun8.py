def Add(a,b):
	return a+b
	
def sub(a,b):
	return a-b


# function accept multiple parameters and call another function from it and return multiple values
def Exellent(value1,value2):
	Ans = Add(value1,value2)
	Sub = sub(value1,value2)
	
	return Ans,Sub
	
def main():
	Arr = Exellent(11,7)
	print("Addition is : ",Arr[0])
	print("Subtraction is : ",Arr[1])
	
if __name__ == "__main__":
	main()
