def addition(no1,no2):
	ans =0
	ans = no1 + no2
	return ans
	
def subtraction(no1,no2):
	ans =0
	ans = no1 - no2
	return ans

def main():
	value1 = int(input("Enter first no. : "))
	value2 = int(input("Enter second no : "))
	
	ret = addition(value1,value2)
	print("addition is : ",ret)
	
	ret = subtraction(value1,value2)
	print("subtraction is : ",ret)
	
if __name__ == "__main__":
	main()
