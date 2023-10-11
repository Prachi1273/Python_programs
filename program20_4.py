def Pattern(row,col):
	for i in range(row,0,-1):
		for j in range(1,col+1):
			print(i,end=" ")
		print()

def main():
	row = int(input("Enter number of rows : "))
	col = int(input("Enter number of columns : "))
	
	Pattern(row,col)

if __name__ == "__main__":
	main()
