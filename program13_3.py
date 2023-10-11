def Digitbet_ThreeSeven(no):
	icnt = 0
	i=0
	dig = 0
	while(no>0):
		dig = no % 10
		if(dig >3 and dig<7):
			icnt = icnt+1
		
		no = int(no/10)
	return icnt

def main():
	no = int(input("Enter a Number : "))
	
	Ans = Digitbet_ThreeSeven(no)
	
	print("No. of Digits between 3 & 7 in ",no,"are : ",Ans)

if __name__ == "__main__":
	main()
	
