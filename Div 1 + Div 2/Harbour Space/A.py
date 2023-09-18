
def solve():
    x = input().split()
    n = int(x[2])
    y = int(x[1])
    x = int(x[0])

    arr = [0] * n

    arr[0] = x
    arr[n-1] = y

    step = 1

    for i in range(n-1, 1, -1):
        arr[i - 1] = arr[i] - step
        step += 1

    if arr[0] >= arr[1] or arr[1] - arr[0] <= arr[2] - arr[1]:
        print(-1)
    else:
        print(" ".join([str(x) for x in arr]))


t = int(input())
for q in range(t):
    solve()