t = int(input())

for q in range(t):
    n = input().split(" ")
    m = int(n[1])
    n = int(n[0])

    words = []
    for i in range(n):
        words.append(input())

    minDiff = 9999999

    for i in range(n):
        for j in range(i+1, n):
            tempDiff = 0
            for k in range(m):
                tempDiff += abs(ord(words[i][k]) - ord(words[j][k]))
            if tempDiff < minDiff:
                minDiff = tempDiff
    print(minDiff)