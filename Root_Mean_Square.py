#software hackathon
import math  
def root_mean_square(number_array, num): 
    square = 0
    mean = 0.0
    root = 0.0
    n = num
    for i in range(0, int(n)): 
        square += (number_array[i]**2)   
    mean = (square / (float)(n))  
    root = math.sqrt(mean) 
    return root
number_array = list()
num = input("Total count of number :")
print ('Enter numbers in array: ')
for i in range(int(num)):
    print("Number",i,str(":"));n = input("")
    number_array.append(float(n))
print(root_mean_square(number_array,num))