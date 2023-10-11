def Pattern(row,col):
	cnt = 1
	for i in range(row,0,-1):
		for j in range(1,col+1):
			print(cnt,end=" ")
			cnt+=1
			if cnt>9:
				cnt = 1
		print()

def main():
	row = int(input("Enter number of rows : "))
	col = int(input("Enter number of columns : "))
	
	Pattern(row,col)

if __name__ == "__main__":
	main()
