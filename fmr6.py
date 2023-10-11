from functools import reduce

def main():
	data = []
	
	print("Enter no. of elements : ")
	size = int(input())
	print("Enter the elements : ")
	for i in range(size):
		value = int(input())
		data.append(value)
		
	print("input data ; ",data)
	
	output = list(filter((lambda no :(no%2==0)),data))
	print("output after filter : ",output)
	
	mop = list(map((lambda no : (no+2)),output))
	print("output after map : ",mop)
	
	result = reduce((lambda a,b : (a+b)),mop)
	print("output after reduced : ",result)
	
if __name__ == "__main__":
	main()
	
"""
Enter no. of elements : 
5
Enter the elements : 
6
7
8
9
5
input data ;  [6, 7, 8, 9, 5]
output after filter :  [6, 8]
output after map :  [8, 10]
output after reduced :  18


"""
