def Display(no):
	if(no<10):
		print("Hello")
	else:
		print("Demo")

def main():
	print("Enter number : ")
	no = int(input())
	
	Display(no)

if __name__ == "__main__":
	main()
