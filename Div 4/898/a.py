
def solve():
    s = input()
    if s == "abc" or s == "acb" or s == "bac" or s == "cba":
        print("YES")
        return
    print("NO")
    return

t = int(input())
for q in range(t):
    solve()