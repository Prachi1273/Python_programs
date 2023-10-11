
def main():
	print("Enter First number : ")
	no1 = int(input())
	
	print("Enter Second number : ")
	no2 = int(input())
	
	Ans = 0
	
	try :
		Ans = no1 / no2
	
	except ZeroDivisionError as zobj:
		print("Divide by zero is not allowed : ",zobj)
	
	print("Division is : ",Ans)

if __name__ == "__main__":
	main()
