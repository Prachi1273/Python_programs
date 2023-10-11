class arithmetic:
	def __init__(self,a,b):
		print("Inside constructor")
		self.no1 = a
		self.no2 = b
		
	def addition(self):
		ans =0
		ans = self.no1 + self.no2
		return ans
		
	def subtraction(self):
		ans =0
		ans = self.no1 - self.no2
		return ans

def main():
	value1 = int(input("Enter first no. : "))
	value2 = int(input("Enter second no : "))
	
	obj1 = arithmetic(value1,value2)
	ret = obj1.addition()
	print("add : ",ret)
	ret = obj1.subtraction()
	print("sub : ",ret)
	
	value1 = int(input("Enter first no. : "))
	value2 = int(input("Enter second no : "))
	
	obj2 = arithmetic(value1,value2)
	ret = obj2.addition()
	print("add : ",ret)
	ret = obj2.subtraction()
	print("sub : ",ret)
	
if __name__ == "__main__":
	main()
