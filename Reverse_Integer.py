a = int(input(""))
b = 0
while a>0:
  temp = a%10
  b = b*10 + temp
  a =a//10
print(b)