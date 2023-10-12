
def solve():
    n = int(input())

    arr = [int(x) for x in input().split()]
    k = int(input())

    ans = [0] * n

    d = {}
    for i in range(n):
        d[i] = arr[i]
    arr = sorted(d.items(), key=lambda x: (x[1], -x[0]))
    print(arr)

    while arr[0][1] <= k:
        furthest = arr[0][0]
        famount = arr[0][1]
        for i in range(1,n):
            if arr[i][0] > furthest and k >= arr[i][1]:
                furthest = arr[i][0]
                famount = arr[i][1]
        if furthest == arr[0][0]:
            val = k // arr[0][1]
            for i in range(arr[0][0] + 1):
                ans[i] += val
            break
        else:
            if k // famount == k // arr[0][1]:
                #end
                val = k // famount
                for i in range(furthest + 1):
                    ans[i] += val
                break
            if k - arr[i][1] < arr[0][1]:
                arr[i][1] = 1000000000
            else:
                val = (k - arr[i][1]) // arr[0][1]
                for i in range(arr[0][0] + 1):
                    ans[i] += val
                k -= (val * arr[0][1])
    zeros = -1
    for i in range(n):
        if ans[i] == 0:
            zeros = i
            break
    ans = " ".join([str(x) for x in ans])
    print(ans, zeros)
    if zeros != -1:
        for i in range(zeros, n):
            ans += " 0"
    print(ans)



t = int(input())
for q in range(t):
    solve()
