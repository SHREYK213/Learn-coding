n=int(input())

fact=1

if n < 0:
    print("not possible")
else:
    for i in range(1,n+1):
        fact*=i
print(fact)