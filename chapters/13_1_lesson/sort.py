import random
def sort(num):
    
    for i in range(len(num)-1):
        print(num[i], num[i+1])
        if num[i]>num[i+1]:
            c = num[i]
            num[i] = num[i+1]
            num[i+1] = c
            
        
        
        print(i)
        print(num)
num = [11,45,65,23,63,24]
sort(num)
sort(num)
sort(num)