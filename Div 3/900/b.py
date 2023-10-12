
def solve():
    n = int(input())
    arr = [6, 7]
    dist = 2
    mdist = 2
    for i in range(2, n):
        num = arr[i - 1] + dist
        arr.append(num)
        dist -= 1
        if dist == 0:
            mdist += 1
            dist = mdist
    print(" ".join([str(x) for x in arr]))
    for i in range(n-2):
        if int(arr[i + 2]) * 3 % (int(arr[i + 1]) + int(arr[i])) == 0:
            print("ERROR")



t = int(input())
for q in range(t):
    solve()