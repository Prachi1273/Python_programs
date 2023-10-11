def Ans(no,ele):
	mult=1
	for i in range(0,ele):
		if(no[i]%2!=0):
			mult=mult*no[i]
			
	return mult
	

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
		
	
	res = Ans(no,ele)
	print("Multiplication of odd numbers : ",res)
if __name__ == "__main__":
	main()
