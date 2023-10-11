def Larger(nums):
	maxi = nums[0]
	for i in range(len(nums)):
		if(nums[i]>maxi):
			maxi = nums[i]
	return maxi

def main():
	no = int(input("Enter no. of elements : "))
	
	eles = list()
	
	print("Enter elements : ")
	
	for i in range(no):
		num = int(input())
		eles.append(num)
		
	maxi=Larger(eles)
	
	print("Larger no. is : ",maxi)

if __name__ == "__main__":
	main()
