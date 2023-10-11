def Display(no):		
	print("Amount in Indian Currency : Rs.",no*70)
	
def main():
	value = int(input("Enter Amount in dollar : "))
	
	Display(value)

if __name__ == "__main__":
	main()
