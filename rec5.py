i=0

def Displayf():
	global i
	print("Inside Display",i)
	i+=1
	Displayf()

def main():
	Displayf()
	

if __name__ == "__main__":
	main()
