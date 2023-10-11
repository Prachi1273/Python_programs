Add = lambda a,b : a+b
	
sub = lambda a,b : a-b


# lambda
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
