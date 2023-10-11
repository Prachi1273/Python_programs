import functools

def main():
	data = []
	
	print("Enter no. of elements : ")
	size = int(input())
	print("Enter the elements : ")
	for i in range(size):
		value = int(input())
		data.append(value)
		
	print("input data ; ",data)
	
	print(functools.reduce(lambda a,b : (a+b),(map(lambda no : (no+2),filter(lambda no :(no%2==0),data)))))
	
if __name__ == "__main__":
	main()
	
"""
Enter no. of elements : 
4
Enter the elements : 
2
3
4
5
input data ;  [2, 3, 4, 5]
10

"""
