import random
def list_ends(a):
    return [a[0], a[len(a)-1]]
a = random.sample(range(1,20),10)
c = [list_ends(a)]
print(a)
print(c)