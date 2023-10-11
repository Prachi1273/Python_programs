		
def Accept():
	print("Enter one number : ")
	no = int(input())
	
	def DisplayEven(no):
		for i in range(2,no,2):
			if(no%i==0):
				print(i)
	
	return DisplayEven(no)

def main():
	Accept()

if __name__ == "__main__":
	main()
