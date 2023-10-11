from functools import reduce

checkeven = lambda no :(no%2==0)	

increase = lambda no : (no+2)
	
add = lambda a,b : (a+b) 

def main():
	data = []
	
	print("Enter no. of elements : ")
	size = int(input())
	print("Enter the elements : ")
	for i in range(size):
		value = int(input())
		data.append(value)
		
	print("input data ; ",data)
	
	output = list(filter(checkeven,data))
	print("output after filter : ",output)
	
	mop = list(map(increase,output))
	print("output after map : ",mop)
	
	result = reduce(add,mop)
	print("output after reduced : ",result)
	
if __name__ == "__main__":
	main()
	
"""
Enter no. of elements : 
5
Enter the elements : 
2
3
4
5
6
input data ;  [2, 3, 4, 5, 6]
output after filter :  [2, 4, 6]
output after map :  [4, 6, 8]
output after reduced :  18

"""
