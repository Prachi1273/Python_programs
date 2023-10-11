#function defines another function inside it
def Exellent(value1,value2):
	def Add(a,b):
		return a+b

	Ans = Add(11,7)
	return Ans
	
	
def main():
	Ans = Exellent(11,7)
	print("Addition is : ",Ans)
	
if __name__ == "__main__":
	main()
