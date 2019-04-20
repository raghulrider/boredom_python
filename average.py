# Read an integer:
val = 0; count =0;
b= []
while(1) :
  a = int(input())
  b.append(a)
  if a > 0:
    count = count + 1
    val = val + a
  else:
      break
for n in b:
  if n<0:
    c = 0.0
  else:
    c = val/count
print(c)