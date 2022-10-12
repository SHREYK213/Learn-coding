import math


n1=int(input())
n2=int(input())

# hcf=1

# for i in range(1,min(n1,n2)):
#     if n1%i ==0 and n2%i ==0:
#         hcf=i
# print("hcf of",n1,n2,"=",hcf)

HCF=math.gcd(n1,n2)

print(HCF)