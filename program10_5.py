def Display(start,end):
		for i in range(end,start-1,-1):
			print(i)

def main():
	start = int(input("Enter Starting point : "))
	
	end = int(input("Enter Ending point : "))
	
	Display(start,end)

if __name__ == "__main__":
	main()
