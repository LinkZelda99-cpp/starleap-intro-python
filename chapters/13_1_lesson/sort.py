import random
def sort(num):
    for j in range(len(num)-1):
        for i in range(len(num)-1):
            # print(num[i], num[i+1])
            if num[i]>num[i+1]:
                c = num[i]
                num[i] = num[i+1]
                num[i+1] = c
            # print(i)
            # print(num)
# num = [11,45,65,23,63,24,23,23,25,27,93,25,25,2457,254,2345,2753,22573,25672]
def random_numbers(n):
    nums = []
    for i in range(n):
        num = random.randint(1,10000)
        nums.append(num)
    return nums
        
number = 0
# while number < 4:
#     sort(num)
#     number += 1
nums = random_numbers(100)
print(nums)
sort(nums)
# nums.sort()
print(nums)