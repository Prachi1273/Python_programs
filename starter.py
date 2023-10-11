import module1
import module2

def main():
	print("Special variable of starter.py is : ",__name__)
	
	module1.DisplayModule1()
	module2.DisplayModule2()

if __name__ == "__main__":
	main()
