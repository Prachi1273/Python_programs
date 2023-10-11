def Pattern(row,col):
	for i in range(1,row+1):
		for j in range(col,0,-1):
			if(j%2==0):
				print("*",end=" ")
			if(j%2!=0):
				print("#",end=" ")
		print()

def main():
	row = int(input("Enter number of rows : "))
	col = int(input("Enter number of columns : "))
	
	Pattern(row,col)

if __name__ == "__main__":
	main()
