
set1 = {11, 78.89, "Hello", True}
print(set1)
#print(set1[1]) #not allowed

for value in set1:
	print(value)

"""for i in range(len(set1)):
	print(set1[i])
	NOT allowed 
	while also NA"""
	
set2 = {11,78,89,11,78}
print(set2)

print("Enter the value that you want to search in set ")
No = int(input())

for val in set2:
	if(No == val):
		print("Element is present")
		break
