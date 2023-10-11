def Pattern(row,col):
	
	for i in range(row,0,-1):
		c = 'a'
		for j in range(1,col+1):
			if i%2!=0:
				print(c,end=" ")
				c = chr(ord(c)+1)
			if i%2==0:
				print(j,end=" ")
		print()

def main():
	row = int(input("Enter number of rows : "))
	col = int(input("Enter number of columns : "))
	
	Pattern(row,col)

if __name__ == "__main__":
	main()
