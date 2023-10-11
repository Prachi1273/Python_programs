class Arithmetic:
	
	def init(self):
		self.value1=0
		self.value2=0
		
	def Accept(self):
		self.value1 = int(input("Enter first number : "))
		self.value2 = int(input("Enter Second number : "))
	
	def Addition(self):
		Add = self.value1 + self.value2
		return Add
		
	def Subtraction(self):
		Sub = self.value1 - self.value2
		return Sub
		
	def Multiplication(self):
		Mult = self.value1 * self.value2
		return Mult
		
	def Division(self):
		Div = self.value1 / self.value2
		return Div
			
def main():
	obj1 = Arithmetic()
	obj2 = Arithmetic()
	
	obj1.Accept()
	
	Ans = obj1.Addition()
	print("Addition is : ",Ans)
	
	Ans = obj1.Subtraction()
	print("Subtraction is : ",Ans)
	
	Ans = obj1.Multiplication()
	print("Multiplication is : ",Ans)
	
	Ans = obj1.Division()
	print("Division is : ",Ans)
	
	obj2.Accept()
	
	Ans = obj2.Multiplication()
	print("Multiplication is : ",Ans)
	
	Ans = obj2.Subtraction()
	print("Subtraction is : ",Ans)
	
	Ans = obj2.Addition()
	print("Addition is : ",Ans)
	
	Ans = obj2.Division()
	print("Division is : ",Ans)

if __name__ == "__main__":
	main()
