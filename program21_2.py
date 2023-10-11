def Pattern(row,col):
	cnt = 1
	for i in range(row,0,-1):
		for j in range(1,col+1):
			if i%2!=0 and j%2==0:
				print(j,end=" ")
			if i%2==0 and j%2!=0:
				print(j,end=" ")
		print()

def main():
	row = int(input("Enter number of rows : "))
	col = int(input("Enter number of columns : "))
	
	Pattern(row,col)

if __name__ == "__main__":
	main()
