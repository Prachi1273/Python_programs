def Display(start,end):
	if(start>end):
		print("Invalid renge")
		return	
	else:
		for i in range(start,end+1):
			if i%2==0 :
				print(i)

def main():
	start = int(input("Enter Starting point : "))
	
	end = int(input("Enter Ending point : "))
	
	Display(start,end)

if __name__ == "__main__":
	main()
