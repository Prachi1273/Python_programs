
def f(no):
	add = 0
	for i in range(1,no+1):
		if(no%i==0 and i!=no):
			add = add + i
	return add
			
	
def main():
	print("Enter number : ")
	no = int(input())	

	ret = f(no)
	
	print(ret)

if __name__ == "__main__":
	main()
