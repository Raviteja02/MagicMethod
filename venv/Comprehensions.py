
#List Comprehension Techniques...

x = [p for p in range(10)]
print(x)

y = []
for p in range(10):
    y.append(p)
print(y)

z = []
for p in range(10,20):
	if p%2 == 0:
		z.append(p*2)
print(z)

a =[p*2 for p in range(10,20) if p%2==0]
print(a)

b = [p*p for p in range(10,20) if p%2!=0]
print(b)


data = "python is a opensource programming language"
words = data.split()
c=[[w.upper(),w.lower(),len(w)] for w in words]
for d in c:
    print(d)

for  e in [[w.upper(),w.lower(),len(w)] for w in "python is a programming language".split()]:print(e)


