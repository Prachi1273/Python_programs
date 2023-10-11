
def summation(arr,size):
	for i in range(0,size):
		if(arr[i]==11):
			return True
			break

def main():
	size = int(input("Enter no. of elements : "))
	
	ele = []
	
	print("Enter Elemnts : ")
	
	for i in range(0,size):
		no = int(input())
		ele.append(no)
		
	res = summation(ele,size)
	if(res == True):
		print("11 is present ")
	else:
		print("11 is NOT present ")

if __name__ == "__main__":
	main()
