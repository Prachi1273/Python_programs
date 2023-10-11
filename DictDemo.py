Batches = {"PPA ": 18500, "Python" : 18700, "LB" : 19000, "Angular ": 19200,"LSP" : 18200, "C#" : 21000}

print(Batches)

print(type(Batches))
print(len(Batches))
print(Batches["Python"])

for val in Batches:
	print(val)
	
for val in Batches:
	print(Batches[val])

for val in Batches:
	print(val, Batches[val])

"""
{'PPA ': 18500, 'Python': 18700, 'LB': 19000, 'Angular ': 19200, 'LSP': 18200, 'C#': 21000}
<class 'dict'>
6
18700
PPA 
Python
LB
Angular 
LSP
C#
18500
18700
19000
19200
18200
21000
PPA  18500
Python 18700
LB 19000
Angular  19200
LSP 18200
C# 21000

"""
