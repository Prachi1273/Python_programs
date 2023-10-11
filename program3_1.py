		
def Accept():
	print("Enter one number : ")
	no = int(input())
	
	def DisplayEven(no):
		icnt=0
		i=1
		while(icnt!=no):
			if(i%2==0):
				print(i)
				icnt+=1
				i+=1
			else:
				i+=1
	
	return DisplayEven(no)

def main():
	Accept()

if __name__ == "__main__":
	main()
