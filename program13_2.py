def OddCount(no):
	icnt = 0
	i=0
	dig = 0
	while(no>0):
		dig = no % 10
		if(dig %2 == 0):
			icnt = icnt+1
		elif(dig == 0):
			icnt = icnt+1
		else:
			i = i+1
		no = int(no/10)
	return i

def main():
	no = int(input("Enter a Number : "))
	
	Ans = OddCount(no)
	
	print("No. of Odd Digits in ",no,"are : ",Ans)

if __name__ == "__main__":
	main()
	
