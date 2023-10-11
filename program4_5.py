from functools import reduce

def primeX(arr):
	for i in range(2,arr+2):
		if(arr%i==0):
			break
		else:
			return arr

mult = lambda no : no*2
	
def maxX(arr):
	no=arr[0]
	for i in range(arr):
		if(no>arr):
			return no

def main():
	size = int(input("Enter size of list : "))
	print("Enter elements which you have to save in list : ")
	arr = []
	
	for i in range(size):
		val=int(input())
		arr.append(val)
	
	print("Input data : ",arr)
	
	ans1 = list(filter(primeX,arr))
	
	print("Output after filter : ",ans1)
	
	ans2 = list(map(mult,ans1))
	
	print("Output after map : ",ans2)
	
	ans3 = reduce(maxX,ans2)
	
	print("Output after reduce : ",ans3)	
	

if __name__ == "__main__":
	main()
