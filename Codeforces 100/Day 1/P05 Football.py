string = input()

bit = string[0]
inrow = 1

flag = False

for i in range(1, len(string)):
    if string[i] is bit:
        inrow += 1
    else:
        inrow = 1
        bit = bit | 1
    if inrow == 7:
        print("YES")
        flag = True
        break

if not flag:
    print("NO")