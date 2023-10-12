
def solve():
    n = input().split()
    k = int(n[1])
    n = int(n[0])

    arr = [int(x) for x in input().split()]
    ans = False
    for i in range(n):
        if arr[i] == k:
            ans = True

    if ans:
        print("YES")
    else:
        print("NO")

t = int(input())
for q in range(t):
    solve()