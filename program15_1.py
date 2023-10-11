
def summation(arr,size):
	icnt=0
	for i in range(0,size):
		if(arr[i]%2==0):
			icnt+=1
	return icnt

def main():
	size = int(input("Enter no. of elements : "))
	
	ele = []
	
	print("Enter Elemnts : ")
	
	for i in range(0,size):
		no = int(input())
		ele.append(no)
		
	Ans = summation(ele,size)
	
	print("Frequency of even elements : ",Ans)

if __name__ == "__main__":
	main()
