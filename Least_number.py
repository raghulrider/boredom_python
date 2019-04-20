# Read an integer:
a =[]
for i in range (1,6):
  n = int(input())
  a.append(n)
a.sort(reverse =True)
print(a[-1])