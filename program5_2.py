class Circle:
	PI = 3.14
	
	def __init__(self):
		self.radius=r=0.0
		self.area=a=0.0
		self.circumference=c=0.0
		
	def Accept(self):
		self.radius=int(input("Enter radius : "))
	
	def Area(self):
		self.area=Circle.PI*self.radius*self.radius
	
	def Circumf(self):
		self.circumference=2*Circle.PI*self.radius
	
	def Display(self):
		print("Radius of Circle : ",self.radius)
		print("Area of Circle : ",self.area)
		print("Circumferrence of circle : ",self.circumference)
			
def main():
	obj1 = Circle()
	obj1.Accept()
	obj1.Area()
	obj1.Circumf()
	obj1.Display()

if __name__ == "__main__":
	main()
