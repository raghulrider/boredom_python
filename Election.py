a = int(input())
b =dict(); h = []
d =[]
for i in range(1,a+1):
    c = input("")
    d = c.split()
    if d[0] not in b:
        b[d[0]] = d[1] 
    else:
        b[d[0]] = int(b[d[0]]) + int(d[1])
for k,v in b.items():
    h.append(k)
    h.sort()
for t in h:
    print(t, b[t])