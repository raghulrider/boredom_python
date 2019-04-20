# Read a list of integers:
a = [s for s in input().split()]
b =dict()
for i in a:
    if i not in b:
        b[i] = 0
    else:
        b[i] = b[i] + 1
    print(b[i])