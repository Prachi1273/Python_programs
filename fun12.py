#function defines another function inside it
def Exellent():
	def Add(a,b):
		return a+b

	return Add
	
	
def main():
	Ans = Exellent()
	ret = Ans(10,7)
	print("Addition is : ",ret)
	
if __name__ == "__main__":
	main()
