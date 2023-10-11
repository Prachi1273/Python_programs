def ChkEvn(value):
	Result = value % 2
	
	if(Result == 0):
		print("Number is even")
	else:
		print("Number is odd")

	
def main():
	Value1 = 0
	
	print("Enter Number : ")
	Value1 = int(input())
	
	ChkEvn(Value1)
		

if __name__ == "__main__":
	main()
