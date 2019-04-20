a = int(input(""))
b = 0
while a>0:
  temp = a%10
  b = b + temp
  a =a//10
print(b)