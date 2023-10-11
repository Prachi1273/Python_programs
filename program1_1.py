def div(no1,no2):
	Ans = 0
	Ans = no1 / no2
	if(no2 == 0):
		return -1
	else:
		return Ans

def main():
	print("Enter first number : ")
	no1 = int(input())
	
	print("Enter second number : ")
	no2 = int(input())

	ret = div(no1,no2)
	print("Division is : ",ret)	
	
if __name__ == "__main__":
	main()
