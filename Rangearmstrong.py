import math

first=int(input())
second=int(input())


def is_Armstrong(val):
    sum = 0

    
    arr = [int(d) for d in str(val)]

    
    for i in range(0, len(arr)):
        sum = sum + math.pow(arr[i], len(arr))

    
    if sum == val:
        print(str(val) + ", ", end="")


for i in range(first, second + 1):
    is_Armstrong(i)