
def main():
	try :
	
		print("Enter First number : ")
		no1 = int(input())
		
		print("Enter Second number : ")
		no2 = int(input())
		
		Ans = 0
	
		Ans = no1 / no2
		
	except ZeroDivisionError as zobj:
		print("Division by Zero is not allowed")
		return
		
	except ValueError as obj1:
		print("Invalid input : ",obj)
		return
	
	except Exception as obj:
		print("Exception occured is  : ",obj)
		return
	
	finally :
		print("Thanku for using application")
	
	print("Division is : ",Ans)

if __name__ == "__main__":
	main()
