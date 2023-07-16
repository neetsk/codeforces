
# UNFINISHED DUE TO BRUTE FORCE BEING TOO SLOW

t = int(input())

def bst(a, presum, sum, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if sum == a[mid]:
            return mid
        elif sum > a[mid]:
            return bst(a, a[mid], sum, low, mid - 1)
        elif sum < a[mid] and a[mid] - sum >= presum - sum:
            return bst(a, a[mid], sum, low, mid - 1)
        elif sum < a[mid] and a[mid] - sum < presum - sum:
            return mid


for q in range(t):
    n = input().split(" ")
    q = int(n[1])
    n = int(n[0])

    a = input().split(" ")
    a = [int(x) for x in a]
    a.sort(reverse=True)

    for i in range(1, n):
        a[i] += a[i - 1] 

    quer = []
    for w in range(q):
        quer.append(int(input()))
    
    print(a)
    for i in range(q):
        print(bst(a, a[(0 + n - 1 )// 2], quer[i], 0, n-1))

