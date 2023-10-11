from functools import reduce

lesgrt= lambda no : (no>=70 and no<=90)

inc10 = lambda no : no+10
	
prod = lambda no,mult : mult*no

def main():
	size = int(input("Enter size of list : "))
	print("Enter elements which you have to save in list : ")
	arr = []
	
	for i in range(size):
		val=int(input())
		arr.append(val)
	
	print("Input data : ",arr)
	
	ans1 = list(filter(lesgrt,arr))
	
	print("Output after filter : ",ans1)
	
	ans2 = list(map(inc10,ans1))
	
	print("Output after map : ",ans2)
	
	ans3 = reduce(prod,ans2)
	
	print("Output after reduce : ",ans3)	
	

if __name__ == "__main__":
	main()
