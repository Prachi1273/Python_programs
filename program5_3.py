def chk(no1,no2):
	if(no1==no2):
		return True
	else:
		return False

def main():
	no1 = int(input("Enter First Number : "))
	no2 = int(input("Enter Second Number : "))
	
	Ans = chk(no1,no2)
	if(Ans == True):
		print(no1,",",no2," are equal")
	else:
		print(no1,",",no2," are NOT equal")


if __name__ == "__main__":
	main()
