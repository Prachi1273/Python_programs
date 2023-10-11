def dig(nums):	
	print("Three digit nums in list are : ")
	for i in range(len(nums)):
		display(nums[i])
		
def display(no):
	dig=0
	icnt = 0
	num = 0
	num = no
	
	while(no!=0):
		dig = no%10
		icnt+=1
		if(icnt==3):
			print(num)
		no = int(no/10)	

def main():
	no = int(input("Enter no. of elements : "))
	
	eles = list()
	
	print("Enter elements : ")
	
	for i in range(no):
		num = int(input())
		eles.append(num)
		
	dig(eles)

if __name__ == "__main__":
	main()
