from collections import deque

def solve():
    n = int(input())
    s = [str(x) for x in input()]
    csize = 1
    clet = s[0]
    msize = 0
    for i in range(1, len(s)):
        if s[i] == clet:
            csize += 1
        else:
            if csize > msize:
                msize = csize
            csize = 1
            clet = s[i]
    if csize > msize:
        msize = csize
    print(msize, n/2)
    if msize > (n / 2):
        print((2 * msize) - n)
        return
    print(n % 2)
    return

    

t = int(input())
for q in range(t):
    solve()