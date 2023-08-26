t = int(input())

for q in range(t):
    n = input().split(" ")
    p = int(n[2])
    x = int(n[1])
    n = int(n[0])

    b = False
    bound = n
    if n % 2 == 0:
        bound = 2 * n
    for i in range(1, min(bound, p+1)):
        if (((i * (i + 1)) / 2) + x) % n == 0:
            print("YES")
            b = True
            break
    if not b:
        print("NO")