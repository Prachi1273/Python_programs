
def f(no):
	for i in range(2,no+1):
		if(no%i==0 and i<no):
			return False
		else:
			return True
			
	
def main():
	print("Enter number : ")
	no = int(input())	

	ret = f(no)
	if(ret == True):
		print("Prime")
	else:
		print("NOT prime")
	

if __name__ == "__main__":
	main()
