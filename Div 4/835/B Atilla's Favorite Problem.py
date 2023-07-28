t = int(input())
 
for x in range(t):
    n = int(input())
    s = input()
 
    ans = 1
    #a = 97
    #z = 22
 
    for i in range(n):
        if ord(s[i]) - 96 > ans:
            ans = ord(s[i]) - 96
    print(ans)