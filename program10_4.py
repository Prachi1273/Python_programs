def Display(start,end):
	if(start>end):
		print("Invalid renge")
		return	
	else:
		add = 0
		for i in range(start,end+1):
			if i<0 :
				return
			if i%2==0:
				add = add+i
		return add

def main():
	start = int(input("Enter Starting point : "))
	
	end = int(input("Enter Ending point : "))
	
	Ans = Display(start,end)
	
	print("Addition of numbers from range ",start ,"to ",end," is : ",Ans)

if __name__ == "__main__":
	main()
