class Demo:
	Value = 11
	
	def __init__(self,no1,no2):
		self.num1=no1
		self.num2=no2
		self.num1=int(input("Enter value of no1 : "))
		self.num2=int(input("Enter value of no2 : "))
		
	def Fun(self):
		print("no1 from Fun = ",self.num1)
		print("no2 from fun = ",self.num2)
		
	def Gun(self):
		print("no1 from gun = ",self.num1)
		print("no2 from gun = ",self.num2)
			

def main():
	obj1 = Demo(11,21)
	obj2 = Demo(51,101)
	
	obj1.Fun()
	obj2.Fun()
	obj1.Gun()
	obj2.Gun()

if __name__ == "__main__":
	main()
