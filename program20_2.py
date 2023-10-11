def Pattern(row,col):
	for i in range(1,row+1):
		ch = 'A'
		c = 'a'
		for j in range(1,col+1):
			if i%2!=0:
				print(ch,end=" ")
				ch = chr(ord(ch)+1)
			if i%2==0:
				print(c,end=" ")
				c = chr(ord(c)+1)
		print()

def main():
	row = int(input("Enter number of rows : "))
	col = int(input("Enter number of columns : "))
	
	Pattern(row,col)

if __name__ == "__main__":
	main()
