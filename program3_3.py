def Dmin(arr,ele):
	min1 = arr[0]
	for i in range(0,ele):
		if(arr[i]<min1):
			min1 = arr[i]
	return min1

def main():
	ele = int(input("Enter number of elements : "))
	
	arr = list()
	
	for i in range(0,ele):
		val = int(input())
		arr.append(val)
		
	ans = Dmin(arr,ele)
	
	print("Minimum number is : ",ans)
	
if __name__ == "__main__":
	main()
