
# Tuple Class Objects # immutable objects

X = ('A','B','C')
print(X)
print(type(X))
print(id(X))

y =('A','B','C')
print(id(y))


print(X[1])



# List Class Objects # mutable objects

z = [10,20,'ravi',3+4j,10.0,True]
print(z)
print(type(z))
print(z[1])
print(z[2])
print(z[3:])
print(z[:4])
print (id(z))

z[2] = 'sri'

print(z)
print(id(z))

z.append('sri')
z.insert(3,'sri')
print(z)

z.pop()
print(z)
z.remove(3+4j)
print(z)

a = z.copy()
print(a)
print(a.index(20))
a.append(20)
print(a)
print(a.index(20,3))

b = [55,66,77]
a.extend(b)
print(a)

a.reverse()
print(a)

c = [10,30,50,20,40]
c.sort()
print(c)

c.clear()
print(c)

d = [[10,20,30],[40,50,60],[60,70,80]]

for e in d:
    for f in e:
         print(f,end = " ")
         print()


for a,b,c in d:
    print(a,b,c)