
def solve():
    n = input().split()
    x = int(n[1])
    n = int(n[0])

    arr = [int(x) for x in input().split()]

    arr.sort()

    sum = 0
    for i in range(n):
        sum += arr[i]

    p = 0
    while True:
        if p > 0:
            sum -= arr[n-p]
        h = arr[n-1]
        m = (h * n) - sum
        if p > 0:
            h = arr[n-p-1]
            m = (h * (n-p)) - sum
        #print(p, h, sum, m)
        if x == m:
            print(h)
            return
        elif x > m:
            x -= m
            h += (x // (n - p))
            print(h)
            return
        else:
            p += 1
        

t = int(input())
for q in range(t):
    solve()