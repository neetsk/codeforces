
def solve():
    n = int(input())
    c = [int(x) for x in input().split()]
    d = {}
    for i in range(n):
        if c[i] not in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    points = 0
    for c,a in d.items():
        if a == 2:
            points += 1
    print(points)

t = int(input())
for i in range(t):
    solve()