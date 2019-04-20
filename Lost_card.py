b =[]
a = int(input())
for i in range (1,a):
  c = input()
  b.append(int(c))
for g in range(1,a+1):
    if g in b:
        continue
    else:
        print(g)
        break