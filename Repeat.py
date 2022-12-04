string=str (input())
index=-1
fnc=""

for i in string :
    if string.count(i)==1:
        fnc += i
        break
    else:
        index+= 1
if index==1:
    print("No repeating")
else:
    print("the duplicate char is :",fnc)