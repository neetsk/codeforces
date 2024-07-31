import math

def solve():
    n = input().split()
    m = int(n[1])
    n = int(n[0])
    x = [str(q) for q in input()]
    s = [str(q) for q in input()]

    OPS = 0
    px = 0
    ps = 0
    start = 0
    while True:
        if s[ps] == x[px]:
            ps += 1
            px += 1
            if ps == m:
                if OPS == 0:
                    print(0)
                else:
                    print(math.ceil(math.log2(OPS + 1)))
                return
        else:
            start += 1
            OPS = 0
            if start == n:
                print(-1)
                return
            ps = 0
            px = start
        if px == n:
            px = 0
            OPS += 1     


t = int(input())
for q in range(t):
    solve()