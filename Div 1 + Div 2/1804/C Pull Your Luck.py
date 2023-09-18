t = int(input())

for q in range(t):
    n = input().split(" ")
    p = int(n[2])
    x = int(n[1])
    n = int(n[0])

    b = False
    bound = n #n * (n + 1) / 2 has a period of n so we stop at n
    if n % 2 == 0: #2n * (2n + 1) / 2 has a period of 2n and not n because n * (n + 1) / 2 is not divisible by n but the other equation is
        bound = 2 * n
    # values after the period are equivalent to going to p = 1, p = 2, etc since we are divisible by n
    # this makes the searching case much smaller than it was before making the problem solveable in given time
    # p is too many wasted cases when it is 1 * 10^9
    for i in range(1, min(bound, p+1)):
        if (((i * (i + 1)) / 2) + x) % n == 0:
            print("YES")
            b = True
            break
    if not b:
        print("NO")