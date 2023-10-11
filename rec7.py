import sys

def main():
	print("Recursiion limit is : ",sys.getrecursionlimit())
	sys.setrecursionlimit(1500)
	print("Recursiion limit is : ",sys.getrecursionlimit())

if __name__ == "__main__":
	main()
