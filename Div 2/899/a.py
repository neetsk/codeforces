def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]

    seq = 1
    for i in range(n):
        if arr[i] == seq:
            seq += 1
        if i == n-1:
            break
        seq += 1
    print(seq)

t = int(input())
for q in range(t):
    solve()