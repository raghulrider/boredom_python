# Read a list of integers:
count = dict()
a = [int(s) for s in input("").split()]
for num in a:
    if num not in count:
        count[num] = 1
    else:
        count[num] = count[num] + 1
for k,v in count.items():
    if v == 1:
        print(k)