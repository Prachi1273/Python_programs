def Display(no):
	if(no<0):
		no = -no
		
	for i in range(no):
		print("* ",end="")
	for i in range(no):
		print("# ",end="")
	print()
	
def main():
	value = int(input("Enter number : "))
	
	Display(value)

if __name__ == "__main__":
	main()
