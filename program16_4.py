def Ans(no,value1,value2,ele):
	icnt=0
	for i in range(0,ele):
		if(no[i]>value1 and no[i]<value2):
			print(no[i])
	

def main():
	print("Enter no. of elements : ")
	ele = int(input())
	
	no = []
	
	print("Enter elements : ")
	
	for i in range(0,ele):
		num = int(input())
		no.append(num)
		
	for i in range(0,len(no)):
		print(no[i])
		
	value1 = int(input("Enter Starting no. : "))
	
	value2 = int(input("Enter ending no. : "))
	
	Ans(no,value1,value2,ele)
if __name__ == "__main__":
	main()
