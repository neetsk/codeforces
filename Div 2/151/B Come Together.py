t = int(input())

for q in range(t):
    n = int(input())
    b = input().split(" ")
    b = [int(x) for x in b]

    k = 0
    k2 = 0
    tot = 0

    for i in range(n):
        tot += b[i]
        if tot > k:
            k2 = k
            k = tot


    print(k, k2)

