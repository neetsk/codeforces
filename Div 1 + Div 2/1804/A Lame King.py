
t = int(input())

for q in range(t):
    x = input().split(" ")
    y = abs(int(x[1]))
    x = abs(int(x[0]))

    if min(y, x) == 0: 
        print(int((max(x, y) - 1) * 2 + 1))
    else:
        nummoves = min(y, x) * 2
        y -= (nummoves / 2)
        x -= (nummoves / 2)
        if max(x, y) != 0:
            nummoves += ((max(x, y) - 1) * 2) + 1
        print(int(nummoves))


    