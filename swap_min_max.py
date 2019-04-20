a = [int(s) for s in input().split()]
b= []
for c in a:
    b.append(c)
a.sort(reverse =True)
maxi = a[0]; mini = a[-1]
for m, k in enumerate(b):
    if k == int(mini):
        b[m] = int(maxi)
    if k == int(maxi):
        b[m] = int(mini)
for j in b:
  print(j)