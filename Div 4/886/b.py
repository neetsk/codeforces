
def solve():
    n = int(input())

    max = 1
    maxp = 1
    for i in range(n):
        temp = input().split()
        if int(temp[0]) <= 10 and int(temp[1]) > max:
            max = int(temp[1])
            maxp = i + 1
    print(maxp)


t = int(input())
for q in range(t):
    solve()
