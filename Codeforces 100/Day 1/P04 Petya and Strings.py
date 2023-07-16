str1 = input()
str2 = input()

'''
flag = False
for i in range(len(str1)):
    if ord(str1[i].upper()) < ord(str2[i].upper()):
        print("-1")
        flag = True
        break
    elif ord(str1[i].upper()) > ord(str2[i].upper()):
        print("1")
        flag = True
        break

if not flag:
    print("0")
'''

if str1.upper() > str2.upper():
    print("1")
elif str2.upper() > str1.upper():
    print("-1")
else:
    print("0")

