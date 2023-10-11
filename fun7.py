def Add(a,b):
	return a+b
	
def sub(a,b):
	return a-b


# function accept multiple parameters and call another function from it
def Exellent(value1,value2):
	Ans = Add(value1,value2)
	print("Addition is : ",Ans)
	Sub = sub(value1,value2)
	print("Subtraction is : ",Sub)
	
def main():
	Exellent(11,7)
	
if __name__ == "__main__":
	main()
