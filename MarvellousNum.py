
def chkPrime(ele,arr):
	add = 0
	for i in range(1,ele):
		if(arr[i]% i==0):
			break;
		else:
			add = add + arr[i]
	return add
