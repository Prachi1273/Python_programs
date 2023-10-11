def Ans(no,value,ele):
	icnt=0
	for i in range(0,ele):
		if(no[i]==value):
			return i
	

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
	
	print(value," is present at ",res,"index in list")

if __name__ == "__main__":
	main()
