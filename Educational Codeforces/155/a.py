def solve():
    n = int(input())
    mono = []
    ans = True
    for i in range(n):
        temp = [int(x) for x in input().split()]
        if i == 0:
            mono = temp
        else:
            if temp[0] >= mono[0] and temp[1] >= mono[1]:
                ans = False
    if ans:
        print(mono[0] - 1)
    else:
        print(-1)
    return

t = int(input())
for q in range(t):
    solve()