def Freq(arr,ele,val):
	icnt = 0
	for i in range(0,ele):
		if(arr[i]==val):
			icnt = icnt+1
	return icnt

def main():
	ele = int(input("Enter number of elements : "))
	
	arr = list()
	
	for i in range(0,ele):
		val = int(input())
		arr.append(val)
		
	no = int(input("Enter number : "))
		
	ans = Freq(arr,ele,no)
	
	print("Frequency is : ",ans)
	
if __name__ == "__main__":
	main()
