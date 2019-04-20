a = int(input())
d =[]; e =[]
for i in range(1,a+1):
        c = input("")
        d.append(c.split())
a1 = int(input())
for j in range(1,a1+1):
    u = input("")
    e.append(u)
for word in e:
    for k in range(0, a):
        if word in d[k]:
            print(d[k][0])