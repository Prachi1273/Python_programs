
# function accept parameter and return parameter
def Exellent(value1,value2):
	if (value1>value2):
		return value1
	else:
		return value2
	
def main():
	ret = Exellent(78,45)
	print("Largest number is : ",ret)
	
	ret = Exellent(34,99)
	print("Largest number is : ",ret)		
	
if __name__ == "__main__":
	main()
