class Demo:
	def __init__(self,value1,value2):
		print("Inside init method")   #constructor
		self.No1 = value1
		self.No2 = value2
		
	def Display(self):
		print("value of no1 : ",self.No1)
		print("Value of no2 : ",self.No2)

def main():
	print("OOP")
	
	obj1 = Demo(10,20)
	obj2 = Demo(11,21)
	
	obj1.Display()
	obj2.Display()

if __name__ == "__main__":
	main()
