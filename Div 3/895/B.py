import math

def solve():
    n = int(input())
    arr = []
    for i in range(n):
        temp = input().split()
        arr.append([int(temp[0]), int(temp[1])])
    arr = sorted(arr)

    pasttrap = (arr[0][1] - 1) // 2
    m = arr[0][0] + pasttrap
    for i in range(1, n):
        if arr[i][0] > m:
            print(m)
            return
        pasttrap = (arr[i][1] - 1) // 2
        tempm = arr[i][0] + pasttrap
        m = min(m, tempm)
    print(m)
        

t = int(input())
for q in range(t):
    solve()
