
def check(a):
    for i in range(len(a)):
        if not (a[i] == "0" or a[i] == "1"):
            return False
    return True

def main():
    a = int(input())
    l = [10, 11, 100, 101, 110, 111]
    if check(str(a)):
        print("YES")
        return
    while(True):
        f = False
        for i in reversed(range(len(l))):
            if a >= l[i] and a % l[i] == 0:
                a = a // l[i]
                if check(str(a)):
                    print("YES")
                    return
                else:
                    f = True
                    break
        if not f:
            print("NO")
            return

t = int(input())
for i in range(t):
    main()