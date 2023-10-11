def max1(no,ele):
	max1 = ele[0]
	for i in range(0,no):
		if(ele[i] > max1):
			max1 = ele[i]
	return max1
			

def main():
	print("Enter number of elements : ")
	no = int(input())
	
	ele = list()
	
	print("Enter elements : ")
	
	for i in range(0,no):
		val = int(input())
		ele.append(val)
		
	ans = max1(no,ele)
	
	print("Maximum number is : ",ans)
	
if __name__ == "__main__":
	main()
