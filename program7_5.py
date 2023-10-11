def Display(no):
	if(no<0):
		no = -no
		
	for i in range(10,0,-1):
		print(no*i)
	
def main():
	value = int(input("Enter number : "))
	
	Display(value)

if __name__ == "__main__":
	main()
