def diff(evens,odds):
	print("Frequency of even elements : ",evens)
	print()
	print("Frequency of odd elements : ",odds)
	print()
	print("Diffrence between Frequency of even & off elements in list : ",(evens-odds))

def summation(arr,size):
	evens=0
	odds=0
	for i in range(0,size):
		if(arr[i]%2==0):
			evens = evens +1
		else:
			odds = odds +1
			
	diff(evens,odds)

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
