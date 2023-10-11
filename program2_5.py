def Display(no):
	if(no % 2 == 0):
		return True
	else:
		return False

def main():
	print("Enter number : ")
	no = int(input())
	
	ret = Display(no)
	
	if(ret == True):
		print("Even")
	else:
		print("Odd")

if __name__ == "__main__":
	main()
