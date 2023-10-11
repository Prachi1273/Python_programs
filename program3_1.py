def Add(no,eles):
	sum1 = 0
	for i in range(0,no):
		sum1 = sum1 + eles[i]

	return sum1

def main():
	no = int(input("Enter no. of elements : "))
	
	eles = list()
	
	print("Enter Elements : ")
	
	for i in range(0,no):
		val = int(input())
		eles.append(val)
		
	sum2 = Add(no,eles)
	
	print("Addition is : ",sum2)

if __name__ == "__main__":
	main()
