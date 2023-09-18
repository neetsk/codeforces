
def solve():
    n = input().split()
    b = int(n[1])
    c = int(n[2])
    a = int(n[0])

    if a + b >= 10 or b + c >= 10 or a + c >= 10:
        print("YES")
    else:
        print("NO")

t = int(input())
for q in range(t):
    solve()
