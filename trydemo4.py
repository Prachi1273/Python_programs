
def main():
	print("Enter First number : ")
	no1 = int(input())
	
	print("Enter Second number : ")
	no2 = int(input())
	
	Ans = 0
	
	try :
		Ans = no1 / no2
	
	except Exception as obj:
		print("Exception occured is  : ",obj)
		return
	
	print("Division is : ",Ans)

if __name__ == "__main__":
	main()
