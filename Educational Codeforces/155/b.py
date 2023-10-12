def solve():
    n = int(input())
    x = [int(p) for p in input().split()]
    y = [int(q) for q in input().split()]

    dx = {}
    dy = {}

    xleft = {}
    yleft = {}

    for i in range(n):
        dx[i] = x[i]
        dy[i] = y[i]
        xleft[i] = 0
        yleft[i] = 0

    x = sorted(dx.items(), key=lambda p: (p[1], p[0]))
    y = sorted(dy.items(), key=lambda p: (p[1], -p[0]))

    pointx = 0
    pointy = 0
    while len(xleft) > 1 or len(yleft) > 1:


    print(x, y)

t = int(input())
for q in range(t):
    solve()