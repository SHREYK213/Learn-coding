def factorial(num):
    fact=1
            
    for i in range (num, 1, -1):
        fact *= i
    return fact/2


n=int(input())
r=int(input())

p=factorial(n)

print(p)