def Display(no):
	i=0
	while(no>0):
		dig = no%10
		no = no / 10
		i=i+1
	print(i)

def main():
	print("Enter number : ")
	no = int(input())
	
	Display(no)

if __name__ == "__main__":
	main()
