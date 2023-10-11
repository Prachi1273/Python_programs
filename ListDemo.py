print("Demonstration of List")

List1 = [10,"Hello", 67.90, True]
print(List1)
print(List1[0])

List2 = [11,78,90,23,11,78]
print(List2)

List2[1] = 56#to chk data is mutable
print(List2)

List2.append(101) #to chk list is mutable
print(List2)

List2.remove(23)
print(List2)

List2.remove(11)
print(List2)

#List2.remove(List2[0])
#print(List2)

"""
[10, 'Hello', 67.9, True]
10
[11, 78, 90, 23, 11, 78]
[11, 56, 90, 23, 11, 78]
[11, 56, 90, 23, 11, 78, 101]
[11, 56, 90, 11, 78, 101]
[56, 90, 11, 78, 101]
"""

