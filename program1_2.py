def chknum(no):
	if(no%2 ==0):
		print("Even number")
	else:
		print("Odd number")

def main():
	print("Enter no. : ")
	var1 = int(input())
	
	chknum(var1)

if __name__ == "__main__":
	main()
