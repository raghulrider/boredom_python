def getprime(num):
    if num == 1:
        prime =True
    elif num == 2:
        prime = True
    for x in range(2,int(num/2)+1):
        if num%x ==0:
            prime = False
        else:
            prime = True
    if prime == True:
        return (print("Prime Number"))
    else:
        return(print("Not a Prime Number"))
while(1):
    usr = (input("Enter the number:"))
    if usr == 'exit':
        print("Thank You")
    else:
        getprime(int(usr))