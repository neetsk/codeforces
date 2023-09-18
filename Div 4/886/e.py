import math

def solve():
    n = input().split()
    c = int(n[1])
    n = int(n[0])

    sum = 0
    sum2 = 0

    arr = [int(x) for x in input().split()]

    for i in range(n):
        sum += (arr[i] * arr[i])
        sum2 += (arr[i] * 2)
    
    a = n
    b = sum2
    c = sum - c

    s = int(math.sqrt((b * b) - (4 * a * c)))
    val = (b - s) / (2 * a)
    if s > b:
        val = (s - b) / (2 * a)
    print(int(val / 2))



t = int(input())
for q in range(t):
    solve()
