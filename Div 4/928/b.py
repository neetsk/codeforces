
def solve():
    n = int(input())
    vals = [0] * n
    for i in range(n):
        q = input()
        for j in range(n):
            if q[j] == "1":
                vals[i] += 1
    for i in range(n):
        if i != 0:
            if vals[i] != 0:
                if vals[i - 1] == vals[i] and vals[i - 1] != 0:
                    print("SQUARE")
                    return
                elif vals[i - 1] != vals[i] and vals[i - 1] != 0:
                    print("TRIANGLE")
                    return

t = int(input())
for i in range(t):
    solve()