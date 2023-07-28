import copy
 
t = int(input())
 
for x in range(t):
    n = int(input())
    nums = input().split(" ")
    nums = [int(x) for x in nums]
 
    min = nums[0]
    peak = -1
    valley = False
    flag = False
 
    for i in range(1, n):
        if not valley and nums[i] <= min:
            min = nums[i]
        elif valley and nums[i] < peak:
            print("NO")
            flag = True
            break
        else:
            peak = nums[i]
            valley = True
    
    if not flag:
        print("YES")
    
    
    #ans = [str(x) for x in ans]
    #print(" ".join(ans))
 