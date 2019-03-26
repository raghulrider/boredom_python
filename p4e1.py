hrs = float(input("Enter Hours:"))
rate =float(input("Enter the rate:"))
if hrs <=40:
    pay = hrs*rate
    print(pay)
elif hrs >40:
    pay = 420.0 + (hrs-40)*rate*1.5
    print(pay)
    
        
