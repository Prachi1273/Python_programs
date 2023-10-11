import MarvellousNum

def ListPrime(ele,arr):
	for i in range(0,ele):
		val = int(input())
		arr.append(val)

def main():
	ele = int(input("Enter number of elements : "))
	
	arr = list()
	
	ListPrime(ele,arr)
	
	print("Elements are : ")
	
	for i in range(0,ele):
		print(arr[i],end = "  ")
		
	ans = MarvellousNum.chkPrime(ele,arr)
	
	print("Addition is : ",ans)
	
if __name__ == "__main__":
	main()
