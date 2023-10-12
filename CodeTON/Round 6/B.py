
def solve():
    n = input().split()
    m = int(n[1])
    n = int(n[0])

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    xmax = a[0]
    for i in range(1, n):
        xmax = xmax ^ a[i]

    xmin = xmax
    
    for i in range(m):
        temp = a[0] | b[i]
        for j in range(1, n):
            temp = (a[j] | b[i]) ^ temp
        if xmin > temp:
            xmin = temp
        elif xmax < temp:
            xmax = temp

    print(xmin, xmax)
        

t = int(input())
for q in range(t):
    solve()
