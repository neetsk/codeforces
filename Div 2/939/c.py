
def solve():
    n = int(input())
    m = []
    val = ((n * (n+1)) // 2)
    r = []
    c = []
    ops = 0
    oplist = []
    for i in range(n):
        t = []
        for j in range(1,n+1):
            t.append(j)
        c.append((i+1) * n)
        r.append((n * (n+1)) // 2)
        m.append(t)
        oplist.append([1, i + 1])
        for i in range(n):
            oplist[ops].append(i + 1)
        ops += 1
    while(ops <= 2 * n):
        change = False
        for i in range(n):
            if c[i] < val:
                c[i] = val
                change = True
                for j in range(n):
                    r[j] -= m[j][i]
                    m[j][i] = j + 1
                    r[j] += m[j][i]
                oplist.append([2, i + 1])
                for i in range(n):
                    oplist[ops].append(i + 1)
                ops += 1
        for i in range(n):
            if r[i] < val:
                r[i] = val
                change = True
                for j in range(n):
                    c[j] -= m[i][j]
                    m[i][j] = j + 1
                    c[j] += m[i][j]
                oplist.append([1, i + 1])
                for i in range(n):
                    oplist[ops].append(i + 1)
                ops += 1
        if not change:
            sum = 0
            for i in range(n):
                sum += r[i]
            print(sum, ops)
            for i in range(ops):
                print(" ".join(str(x) for x in oplist[i]))
            return
    sum = 0
    for i in range(n):
        sum += r[i]
    print(sum, ops)
    for i in range(ops):
        print(" ".join(str(x) for x in oplist[i]))
    return


t = int(input())
for i in range(t):
    solve()