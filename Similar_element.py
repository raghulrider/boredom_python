c =[]
a = [int(s) for s in input().split()]
b = [int(t) for t in input().split()]
for i in a:
    if i in b:
        c.append(i)
c.sort()
for k in c:
    print(k)