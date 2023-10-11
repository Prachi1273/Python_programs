def Add(a,b):
	return a+b

#function accepts parameter as another function 
def Exellent(FPTR):
	print(type(FPTR))
	print(FPTR)
	Ans = FPTR(11,7)
	print("Addition is : ",Ans)

	
def main():
	Exellent(Add)
	
	
if __name__ == "__main__":
	main()
