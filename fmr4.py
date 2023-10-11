#unnamed function (lambda function / anonymous function)
#name = lambda parameters_list : function_logic

def add(no1,no2):
	return no1+no2
	
addx = lambda no1,no2 :  no1+no2

def chkeven(no):
	return (no%2 == 0)
	
chkevenx = lambda no : (no%2 == 0)
	
def increase(no):
	return no+2
	
increasex = lambda no : (no+2)

def main():
	ret = add(10,11)
	print(ret)
	ret = chkeven(10)
	print(ret)
	ret = increase(10)
	print(ret)
	
	ret = addx(10,11)
	print(ret)
	ret = chkevenx(10)
	print(ret)
	ret = increasex(10)
	print(ret)

if __name__ == "__main__":
	main()
	
"""
21
True
12
21
True
12

"""
