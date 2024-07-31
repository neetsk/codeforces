
def solve():
    x = input()
    countA = 0
    for i in range(5):
        if x[i] == "A":
            countA += 1
    if countA >= 3:
        print("A")
    else:
        print("B")
    return

t = int(input())
for i in range(t):
    solve()