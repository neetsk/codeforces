t = int(input())

for q in range(t):
    a = input().split(" ")
    b = int(a[1])
    a = int(a[0])

    if a > 1:
        print(a - 1)
    elif b > 2:
        print(2)
    else:
        print(6)
