def Display(no,f):
	for i in range(0,f):
		print(no)

def main():
	print("Enter number : ")
	no = int(input())
	
	print("Enter frequency : ")
	freq = int(input())
	
	Display(no,freq)

if __name__ == "__main__":
	main()
