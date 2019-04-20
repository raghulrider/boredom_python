a = int(input())
b =dict();
d =[]
flag =0
for i in range(1,a+1):
        c = input("")
        d.append(c.split())
for var in range(0,a):
    for j in d[var]:    
        if j not in b:
            b[j] = 1 
        else:
            b[j] = b[j] + 1 
maxword = None
maxcount = 0
temp = []
for k,v in b.items():
    temp.append(k)
    temp.sort()
tempdict = dict()
for ke in temp:
  tempdict[ke] = b[ke]
for key, value in tempdict.items():
  if value > maxcount:
        maxword = key
        maxcount = value
print(maxword)