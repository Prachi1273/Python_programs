
def f(no):
	fact = 1
	for i in range(1,no+1):
		fact = fact * i
	return fact	
	
def main():
	print("Enter number : ")
	no = int(input())
	

	ret = f(no)
	
	print(ret)

if __name__ == "__main__":
	main()
