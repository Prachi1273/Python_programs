from functools import reduce

checkeven = lambda no :(no%2==0)	

increase = lambda no : (no+2)
	
add = lambda a,b : (a+b) 

#task = name of function
#elements = list of data elements 

def filterx(task,elements):
	result = []
	for no in elements:
		if(task(no) == True):
			result.append(no)
	return result

def mapx(task,elements):
	result = []
	for no in elements:
		ret = task(no)
		result.append(ret)
	return result
	
def reducex(task,elements):
	sum = 0
	for no in elements:
		sum = task(sum,no)
	return sum

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
	

