import sys

def Display(no):
	if(no>0):
		print(no)
		Display(no)

def main():
	Display(5)
if __name__ == "__main__":
	main()
