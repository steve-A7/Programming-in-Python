import copy

a=[[1,2],[3,4]]

b=copy.deepcopy(a)
b[0].append(5)

print(id(a))
print(id(b))

print(a)
print(b)

c=10

c + 2

print(c)