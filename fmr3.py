from functools import reduce

def checkeven(no):
	return (no%2==0)

def increase(no):
	return no+2
	
def add(a,b):
	return a+b

def main():
	data = []
	
	print("Enter no. of elements : ")
	size = int(input())
	print("Enter the elements : ")
	for i in range(size):
		value = int(input())
		data.append(value)
	#print(data)
	
	output = list(filter(checkeven,data))
	print(output)
	
	mop = list(map(increase,output))
	print(mop)
	
	result = reduce(add,mop)
	print(result)
	
if __name__ == "__main__":
	main()
