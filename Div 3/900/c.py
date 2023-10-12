
def solve():
    n = input().split()
    x = int(n[2])
    k = int(n[1])
    n = int(n[0])

    print((k * (k + 1)) / 2, ((n * (n + 1)) / 2) - (((n - k) * (n - k + 1)) / 2))
    if (k * (k + 1)) / 2 <= x and ((n * (n + 1)) / 2) - (((n - k) * (n - k + 1)) / 2) >= x:
        print("YES")
    else:
        print("NO")

t = int(input())
for q in range(t):
    solve()