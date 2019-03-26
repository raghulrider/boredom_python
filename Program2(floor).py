a = input("Coversion\n 1.Europe to US\n 2.US to Europe\n Select either 1 or 2:\n")
if a==1:
    eur = input("Enter the Europe Floor:\n")
    us = int(eur)+1
    print("US Floor is, ",us)
else:
    us1 = input("Enter the US Floor:\n")
    eur1 = int(us1)-1
    print("Europe Floor is, ",eur1)