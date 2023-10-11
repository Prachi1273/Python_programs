
def main():
	print("Enter Number : ")
	Value1 = int(input())
	
	Result = Value1 % 2
	
	if(Result == 0):
		print("Number is even")
	else:
		print("Number is odd")

if __name__ == "__main__":
	main()
