
def solve():
    x = input().split()
    a = [int(s) for s in input().split()]
    q = [int(r) for r in input().split()]
    for i in range(int(x[1])):
        if q[i] == a[0]:
            q[i] = q[i] - 1
        elif q[i] > a[0]:
            q[i] = a[0] - 1
    print(" ".join((str(x) for x in q)))

t = int(input())
for i in range(t):
    solve()