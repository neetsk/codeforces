from collections import deque
t = int(input())

'''
for q in range(t):
    n,m = map(int, input().split())
    piles = deque([n]) #queue
    #1/3 + 2/3 = 3/3 so always check / 3
    flag = False
    while(len(piles) > 0):
        #print(piles)
        if piles[0] == m:
            print("YES")
            flag = True
            break
        if piles[0] % 3 == 0:
            piles.append(piles[0] / 3)
            piles.append(2 * (piles[0] / 3))
            #if (piles[0] / 3) == m or (2 * (piles[0] / 3)) == m:
            #    print("YES")
            #    flag = True
            #    break
        piles.popleft()
    if not flag:
        print("NO")
'''
def solve(n, m):
    if n == m:
        return True
    if m > n:
        return False
    if n % 3 != 0:
        return False
    return solve(n // 3, m) or solve(2 * (n // 3), m)

for q in range(t):
    n,m = map(int, input().split())
    ans = solve(n, m)
    if ans:
        print("YES")
    else:
        print("NO")





