
def solve():
    n = int(input())
    arr = []
    for i in range(n):
        x = [ord(q) for q in input()]
        arr.append(x)

    op = 0
    val = 0
    bord = 0
    while True: #fix
        m = max(arr[bord][val], arr[val][n-1-bord], arr[n-1-val][bord], arr[n-1-bord][n-1-val])
        op += (m - arr[bord][val])
        op += (m - arr[val][n-1-bord])
        op += (m - arr[n-1-val][bord])
        op += (m - arr[n-1-bord][n-1-val])
        val += 1
        if val == n-1-bord:
            bord += 1
            if bord == (n / 2):
                print(op)
                return
            val = bord
        

t = int(input())
for q in range(t):
    solve()