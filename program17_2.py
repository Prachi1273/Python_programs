def Larger(nums):
	mini = nums[0]
	for i in range(len(nums)):
		if(nums[i]<mini):
			mini = nums[i]
	return mini

def main():
	no = int(input("Enter no. of elements : "))
	
	eles = list()
	
	print("Enter elements : ")
	
	for i in range(no):
		num = int(input())
		eles.append(num)
		
	mini=Larger(eles)
	
	print("Smaller no. is : ",mini)

if __name__ == "__main__":
	main()
