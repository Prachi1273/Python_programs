from functools import reduce
from fmr import filterx
from fmr import mapx
from fmr import reducex
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
	
	output = list(filterx(checkeven,data))
	print("output after filter : ",output)
	
	mop = list(mapx(increase,output))
	print("output after map : ",mop)
	
	result = reducex(add,mop)
	print("output after reduced : ",result)
	
if __name__ == "__main__":
	main()
	

