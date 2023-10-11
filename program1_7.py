def chknum(no):
	if(no%5==0):
		print("True")
	else:
		print("False")

def main():
	print("Enter number : ")
	num = int(input())
	
	chknum(num)

if __name__ == "__main__":
	main()
