from functools import reduce
import fmr
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
	
	output = list(fmr.filterx(checkeven,data))
	print("output after filter : ",output)
	
	mop = list(fmr.mapx(increase,output))
	print("output after map : ",mop)
	
	result = fmr.reducex(add,mop)
	print("output after reduced : ",result)
	
if __name__ == "__main__":
	main()
	

