def MultDig(no):
	mult = 1
	dig = 0
	while(no>0):
		dig = no % 10
		if(dig==0):
			dig = 1
		mult = mult*dig
		no = int(no/10)
	return mult

def main():
	no = int(input("Enter a Number : "))
	
	Ans = MultDig(no)
	
	print("Multiplication of digits in",no,"are : ",Ans)

if __name__ == "__main__":
	main()
	
