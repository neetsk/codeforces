
def solve():
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    groups = 1
    for i in range(1, n):
        for j in range(i):
            print(arr[j], arr[i], arr[j] &arr[i])
            if arr[j] & arr[i] != 0:
                groups += 1
                break
    print("GROUPS", groups)
    return

t = int(input())
for i in range(t):
    solve()