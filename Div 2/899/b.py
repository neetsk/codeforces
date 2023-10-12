

def solve():
    n = int(input())

    s = []
    for i in range(n):
        size = [int(x) for x in input().split()]
        s.append(set(size[1:]))

    s.sort(key=lambda x: len(x), reverse=True)

    lconsidered = len(s[0])
    while len(s) > 0:
        common = s[0]
        skip = False
        for i in range(1, len(s)):
            common = common & s[i]
            if len(s) == n-1:
                lconsidered += len(s[i])
            if len(common) == 0:
                s.remove(s[i])
                skip = True
                break
        if not skip:
            if len(common) != 0:
                if len(s) == n:
                    print("ans", lconsidered - len(s[n-1]))
                else:
                    temp = set()
                    for i in range(len(s)):
                        temp = temp | s[i]
                    print("ans", len(temp))
                return
    print("ans", 0)


t = int(input())
for q in range(t):
    solve()