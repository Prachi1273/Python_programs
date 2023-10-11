def chk(no):
	if(no>100):
		return True
	else:
		return False

def main():
	no = int(input("Enter Number : "))
	
	Ans = chk(no)
	if(Ans == True):
		print(no," is Greater than 100")
	else:
		print(no," is smaller than 100")

if __name__ == "__main__":
	main()
