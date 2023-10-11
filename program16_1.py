def Ans(no,value,ele):
	icnt=0
	for i in range(0,ele):
		if(no[i]==value):
			icnt+=1
	
	if icnt>=1:
		return True
	else:
		return False

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
		
	value = int(input("Enter one another no. : "))
	
	res = Ans(no,value,ele)
	if res==True:
		print(value," is present in list")
	else:
		print(value," is NOT present in list")

if __name__ == "__main__":
	main()
