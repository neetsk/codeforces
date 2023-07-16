t = int(input())

for q in range(t):
    n = int(input())
    s = input().split(' ')
    s = [int(x) for x in s]

    minNum = min(s)
    toEat = 0

    for i in range(n):
        toEat += s[i] - minNum
    print(toEat)
        