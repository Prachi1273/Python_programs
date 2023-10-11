
def Sub(A,B):
	return A-B

def smartsub(fptr):
	def Inner(A,B):
		if(A<B):
			A,B = B,A
		return fptr(A,B)
	return Inner
		
	
def main():
	Subx = smartsub(Sub)
	
	Ret = Subx(10,7)
	print("Subtraction is : ",Ret)
	
	Ret = Subx(7,10)
	print("Subtraction is : ",Ret)
	
if __name__ == "__main__":
	main()
