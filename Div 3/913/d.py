plat = []

def check(k):
    print("check", k)
    posl = 0
    posr = 0
    for i in range(len(plat)):
        if posr > plat[i][0]
            return False
        else:
            posr = min(plat[i][1], posr + k)
            posl = max(plat[i][0], posl - k)
            print(posl, posr)
    print('true')
    return True

def binsearch(l, r, last):
    while l <= r:
        print(l, r, last)
        mid = (r - l) // 2
        diff = abs(last - mid)
        res = check(mid)
        if res:
            r = mid - 1
        elif not res and diff > 1:
            l = mid + 1
        else:
            return last

def solve():
    n = int(input())
    for i in range(n):
        temp = input().split()
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        plat.append(temp)
    print(binsearch(0, 1000000000 - 1, 0))
    

t = int(input())
for q in range(t):
    solve()