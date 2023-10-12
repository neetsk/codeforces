
def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]

    min = 10
    ind = 0
    for i in range(n):
        if arr[i] < min:
            ind = i
            min = arr[i]

    arr[ind] += 1
    ans = 1
    for i in range(n):
        ans *= arr[i]
    print(ans)

t = int(input())
for q in range(t):
    solve()