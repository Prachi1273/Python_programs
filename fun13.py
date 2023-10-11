#function defines another function inside it
def Exellent(value1,value2):
	def Add(a,b):
		return a+b

	return Add(value1,value2)
	
	
def main():
	Ans = Exellent(10,7)
	print("Addition is : ",Ans)
	
if __name__ == "__main__":
	main()
