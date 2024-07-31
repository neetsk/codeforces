
def addDiv(x, div):
    i = 2
    while (i * i <= x):
        while(x % i == 0):
            if i in div:
                div[i] += 1
            else:
                div[i] = 1
            x = x // i
        i += 1
    if x > 1:
        if x in div:
            div[x] += 1
        else:
            div[x] = 1

def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]

    div = {}

    for x in arr:
        addDiv(x, div)

    for x in div.items():
        if x[1] % n != 0:
            print("NO")
            return
    print("YES")


t = int(input())
for q in range(t):
    solve()