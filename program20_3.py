def Pattern(row,col):
	ch = '@'
	for i in range(1,row+1):
		ch = chr(ord(ch)+1)
		for j in range(1,col+1):
			print(ch,end=" ")
		print()

def main():
	row = int(input("Enter number of rows : "))
	col = int(input("Enter number of columns : "))
	
	Pattern(row,col)

if __name__ == "__main__":
	main()
