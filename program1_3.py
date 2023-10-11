def Add(no,num):
	Ans = 0
	Ans = no + num
	return Ans

def main():
	print("Enter first no. : ")
	var1 = int(input())
	print("enter second number : ")
	var2 = int(input())
	
	ret = Add(var1,var2)
	print("Addition is : ",ret)

if __name__ == "__main__":
	main()
