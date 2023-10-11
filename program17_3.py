def Larger(nums):
	mini = nums[0]
	maxi=nums[0]
	for i in range(len(nums)):
		if(nums[i]<mini):
			mini = nums[i]
		elif(nums[i]>maxi):
			maxi = nums[i]
	
	print("Largest no. is : ",maxi)
	print("Smallest no. is : ",mini)
	
	return (maxi-mini)

def main():
	no = int(input("Enter no. of elements : "))
	
	eles = list()
	
	print("Enter elements : ")
	
	for i in range(no):
		num = int(input())
		eles.append(num)
		
	ans=Larger(eles)
	
	print("Diffrence betn Larger & Smaller no. is : ",ans)

if __name__ == "__main__":
	main()
