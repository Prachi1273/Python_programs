def Pattern(no):
	ch = 'A'
	for i in range(no):
		print(ch)
		ch = chr(ord(ch)+1)

def main():
	no = int(input("Enter number : "))
	
	Pattern(no)

if __name__ == "__main__":
	main()
