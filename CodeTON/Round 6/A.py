
def solve():
    n = input().split()
    k = int(n[1])
    x = int(n[2])
    n = int(n[0])

    if k - x >= 2 or k - n >= 1:
        print(-1)
        return

    sum = int(((k - 1) * k) / 2)

    n -= k
    if x == k:
        sum += int((n *(k-1)))
    else:
        sum += int((n * x))
    print(sum)


t = int(input())
for q in range(t):
    solve()
