
def summation(arr,size):
	icnt = 0
	for i in range(0,size):
		if(arr[i]==11):
			icnt +=1
	return icnt

def main():
	size = int(input("Enter no. of elements : "))
	
	ele = []
	
	print("Enter Elemnts : ")
	
	for i in range(0,size):
		no = int(input())
		ele.append(no)
		
	res = summation(ele,size)

	print("11 is present at ",res," times")

if __name__ == "__main__":
	main()
