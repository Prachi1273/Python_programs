def chknum(no):
	if(no==0):
		print("Zero")
	elif(no>0):
		print("Positive number")
	elif(no<0):
		print("Negative number")
	

def main():
	print("Enter number : ")
	num = int(input())
	
	chknum(num)

if __name__ == "__main__":
	main()
