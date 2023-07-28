import copy
 
t = int(input())
 
for x in range(t):
    n = int(input())
    nums = input().split(" ")
    nums = [int(x) for x in nums]
 
    max1 = max(nums)
    temp = copy.deepcopy(nums)
    temp.remove(max1)
    max2 = max(temp)
    
    ans = []
 
    if nums.count(max1) > 1:
        for i in range(n):
            ans.append(nums[i] - max1)
    else:
        for i in range(n):
            if nums[i] == max1:
                ans.append(max1 - max2)
            else:
                ans.append(nums[i] - max1)
    
    ans = [str(x) for x in ans]
    print(" ".join(ans))