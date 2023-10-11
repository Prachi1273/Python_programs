
Tuple1 = (11, "Hello", 90.89, False)
print(Tuple1)

print(type(Tuple1))
print(len(Tuple1))

print(Tuple1[1])

#Tuple1[0] = 12 #immutable so we cant change value
#print(Tuple1)

#Tuple1.append(67) #no attribute append

tuple2 = (11,89,11,67,11)
print(tuple2)

for value in tuple2:
	print(value)
	
print("-------------")

for i in range(len(tuple2)):
	print(tuple2[i])
	
for i in range(len(tuple2)):
	print(i)
	
"""
(11, 'Hello', 90.89, False)
<class 'tuple'>
4
Hello
(11, 89, 11, 67, 11)
11
89
11
67
11
-------------
11
89
11
67
11
0
1
2
3
4

"""
