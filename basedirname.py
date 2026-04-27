import os

base = os.path.basename('/home/prachi/Pictures/photo.jpg')

dirnm = os.path.dirname('/home/prachi/Pictures/photo.jpg')

head, tail = os.path.split('/home/prachi/Pictures/photo.jpg')

print(base)
print(tail)

print(dirnm)
print(head )

