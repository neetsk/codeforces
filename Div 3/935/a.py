import math

def solve():
    a = input().split()
    b = int(a[1])
    c = int(a[2])
    ans = int(a[0])
    ans += (b // 3)
    if b % 3 != 0:
        if (b % 3) + c < 3:
            print(-1)
            return
        c -= (3 - (b % 3))
        ans += 1
    ans += math.ceil(c / 3)
    print(ans)
    return

t = int(input())
for i in range(t):
    solve()