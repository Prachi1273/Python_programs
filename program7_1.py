def Num(value):
	if(value<50):
		print("Small")
	if(value>50 and value<100):
		print("Medium")
	if(value>100):
		print("Large")

def main():
	print("Enter any number : ")
	value = int(input())
	
	Num(value)

if __name__ == "__main__":
	main()	
