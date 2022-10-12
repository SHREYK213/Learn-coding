from math import gcd
import math


n1 = int(input())
n2 = int(input())

HCF=math.gcd(n1,n2)
LCM=int((n1*n2)/(HCF))

print(LCM)
