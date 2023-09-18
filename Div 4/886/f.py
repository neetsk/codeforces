
def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]

    arr.sort()

    for i in range(n):
        if arr[i] > n:
            arr = arr[0:i]
            break
    print(arr)

    



t = int(input())
for q in range(t):
    solve()
