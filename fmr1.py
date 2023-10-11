from functools import reduce

def checkeven(no):
	if(no%2==0):
		return True
	else:
		return False

def increase(no):
	return no+2
	
def add(a,b):
	return a+b

def main():
	data = [5,4,9,8,13,17,12,18]
	print(data)
	
	output = list(filter(checkeven,data))
	print(output)
	
	mop = list(map(increase,output))
	print(mop)
	
	result = reduce(add,mop)
	print(result)
	
if __name__ == "__main__":
	main()
