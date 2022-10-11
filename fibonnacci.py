num= int(input())

x=0
y=1
print("the fibbonacci numbers are",x,y, end=" ")
for i in range (2,num):
    z=x+y
    y=z
    x=y
    print(z,end=" ")