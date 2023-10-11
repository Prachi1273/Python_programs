def DisplayFreq(no):
	icnt=0
	for dig in str(no):
		dig = no %10
		if(dig==4):
			icnt+=1
		no = no//10
	return icnt

def main():
	no = int(input("Enter number : "))
	
	Ans = DisplayFreq(no)
	
	print("Frequency of four is : ",Ans)

if __name__ == "__main__":
	main()
