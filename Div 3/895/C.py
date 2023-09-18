
def gcd(a, b):
    if b >= a:
        temp = a
        a = b
        b = temp
    # a > b
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b
def findgcd(val):
    a = 3
    b = val - 3
    while a <= b:
        temp = gcd(a, b)
        if temp != 1:
            return a, b
        m = b % a
        a += m
        b -= m
    return -1, -1

def solve():
    l = input().split()
    r = int(l[1])
    l = int(l[0])

    val = 0
    if r != l:
        if r % 2 == 0:
            val = r
        else:
            val = r - 1
        if val <= 2:
            print(-1)
            return
        print(2, val - 2)
    elif r == l and r % 2 == 0:
        val = r
        if val <= 2:
            print(-1)
            return
        print(2, val - 2)
    else:
        val = r
        temp = findgcd(val)
        if temp[0] == -1:
            print(-1)
            return
        print(temp[0], temp[1])

t = int(input())
for q in range(t):
    solve()

