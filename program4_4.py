from functools import reduce

evenno= lambda no : (no%2==0)

squarex = lambda no : no**2
	
add = lambda no,add : add+no

def main():
	size = int(input("Enter size of list : "))
	print("Enter elements which you have to save in list : ")
	arr = []
	
	for i in range(size):
		val=int(input())
		arr.append(val)
	
	print("Input data : ",arr)
	
	ans1 = list(filter(evenno,arr))
	
	print("Output after filter : ",ans1)
	
	ans2 = list(map(squarex,ans1))
	
	print("Output after map : ",ans2)
	
	ans3 = reduce(add,ans2)
	
	print("Output after reduce : ",ans3)	
	

if __name__ == "__main__":
	main()
