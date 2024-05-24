a = 1
b = a
print(id(a))
print(id(b))
b = b + 1
print(a)
print(b)
print(id(a))
print(id(b))