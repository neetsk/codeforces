
def solve():
    n = input().split()
    k = int(n[1])
    n = int(n[0])

    arr = [str(x) for x in input()]

    ops = 0
    check = 0
    for i in range(n):
        if arr[i] == 'B' and check == 0:
            check = k
            ops += 1
        if check > 0:
            check -= 1
    print(ops)

t = int(input())
for q in range(t):
    solve()