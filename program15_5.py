
def summation(arr,size,val):
	icnt = 0
	for i in range(0,size):
		if(arr[i]==val):
			icnt +=1
	return icnt

def main():
	size = int(input("Enter no. of elements : "))
	
	ele = []
	
	print("Enter Elemnts : ")
	
	for i in range(0,size):
		no = int(input())
		ele.append(no)
		
	val = int(input("Enter no. to search : "))
		
	res = summation(ele,size,val)

	print(val," is present at ",res," times")

if __name__ == "__main__":
	main()
