import math
t = int(input())

for q in range(t):
    n = input().split(" ")
    momentsp = int(n[3])
    momentsv = int(n[2])
    doses = int(n[1]) 
    n = int(n[0])

    p = [int(x) for x in input().split()]

    numpacks = 0
    remainingdoses = 0
    dosetime = 0

    left = 0
    right = 0
    maxtime = p[left] + momentsp + momentsv
    while right < n:
        if remainingdoses == 0:
            numpacks += 1
            remainingdoses = doses
            left = right
            maxtime = p[left] + momentsp + momentsv
        elif p[right] <= maxtime:
            right += 1
            remainingdoses -= 1
        else:
            remainingdoses = 0
    print(numpacks)



    