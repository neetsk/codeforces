
def solve():
    n = input().split()
    k = int(n[1])
    n = int(n[0])
    
    arr = [int(x) for x in input().split()]

    arr.sort()

    if n == 1:
        print(0)
        return
    
    p = 0
    q = 1
    ra = []
    count = 0
    mcount = 0
    while q < n:
        if arr[q] - arr[q - 1] <= k:
            count += 1
            q += 1
        else:
            if count > mcount:
                ra = [count, p, q-1]
                mcount = count
            count = 0
            p = q
            q += 1
    if count > mcount:
        ra = [count, p, q-1]
        mcount = count

    if mcount == 0:
        print(n - 1)
        return
    print(n - ra[0] - 1)
    return


t = int(input())
for q in range(t):
    solve()
