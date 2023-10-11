def CalcPer(Total,Marks):
	Per = (Marks/Total)*100
	return Per

def main():
	Total = int(input("Enter Total Marks : "))
	Marks = int(input("Enter Obtained Marks : "))
	
	Ans = CalcPer(Total,Marks)
	
	print("Percentage : ",Ans,"%")

if __name__ == "__main__":
	main()
