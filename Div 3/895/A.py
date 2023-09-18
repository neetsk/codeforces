import math

def solve():
    a = input().split()
    b = int(a[1])
    c = int(a[2])
    a = int(a[0])

    print(math.ceil((max(a, b) - min(a, b)) / (2*c)))


t = int(input())
for q in range(t):
    solve()
