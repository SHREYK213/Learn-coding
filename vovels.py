string = (input())
count = 0
string = string.lower()

for i in string:
    # char_list = ['a', 'e', 'i', 'o', 'u']
    if i == 'a' or i == 'e' or i == 'o' or i == 'u':
        count += 1
if count == 0:
    print("there are no vovels")
else:
    print("The vovels count is:" + str(count))
