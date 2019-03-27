import random
a = random.sample(range(1,20),19)
b = random.sample(range(1,25),24)
c = [x for x in a if x in b]
result = []
for element in c:
    if element not in result:
        result.append(element)
print(c)
print(result)