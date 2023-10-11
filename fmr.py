
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
