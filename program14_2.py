
def summation(arr,size):
	evens=0
	odds=0
	print("Elements divisible by 5 are : ")
	for i in range(0,size):
		if(arr[i]%5==0):
			print(arr[i])

def main():
	size = int(input("Enter no. of elements : "))
	
	ele = []
	
	print("Enter Elemnts : ")
	
	for i in range(0,size):
		no = int(input())
		ele.append(no)
		
	summation(ele,size)

if __name__ == "__main__":
	main()
