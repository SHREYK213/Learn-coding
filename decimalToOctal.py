n=int(input())

octal=[]

while n> 0:
    r= n % 8
    octal.append(r)
    n=n//8
for i in reversed (octal):
    print(i ,end="")