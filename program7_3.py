def Display(no):
	if(no<0):
		no = -no

	if(no ==0):
		print("Zero")
	elif(no ==1):
		print("One")
	elif(no ==2):
		print("Two")
	elif(no ==3):
		print("Three")	
	elif(no ==4):
		print("Four")
	elif(no ==5):  
		print("Five")
	elif(no ==6):
		print("Six")
	elif(no ==7):
		print("seven")
	elif(no ==8):
		print("Eight")
	elif(no ==9):
		print("Nine")
	else:
		print("Not single digit")
	
def main():
	value = int(input("Enter number : "))
	
	Display(value)

if __name__ == "__main__":
	main()
