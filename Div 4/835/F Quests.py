
def solve():
    n = input().split()
    c = int(n[1])
    d = int(n[2])
    n = int(n[0])

    arr = input().split()
    for i in range(n):
        arr[i] = int(arr[i])

        if arr[i] > c:
            print("Infinity")
            return

    arr.append(0)
    arr.sort()
    

    # if we use the max all days, then we have left over coins to use
    leftover = (arr[len(arr) - 1] * d) - c
    if leftover < 0:
        print("Impossible")
        return
    
    k = 0
    for i in range(n-1):
        if leftover - arr[i] > 0:
            k += 1


t = int(input())
for q in range(t):
    solve()

'''
t = int(input())
for q in range(t):
    if solve():
        print("YES")
    else:
        print("NO")

'''