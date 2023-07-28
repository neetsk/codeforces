import copy
 
t = int(input())
 
for x in range(t):
    n = int(input())
    nums = input().split(" ")
    nums = [int(x) for x in nums]
 
    first0 = -1
    #two0 = -1
    last1 = -1
    num1s = 0
    num0s = 0
    score = 0
    for i in range(n):
        if nums[i] == 1:
            last1 = i
            num1s+=1
        else:
            if first0 == -1:
                first0 = i
            else:
                two0 = i
            if num1s != 0:
                score += num1s * 1
            num0s+=1
 
    # flip first 0 to 1 to max score
    opt1flip = score - first0 + num0s - 1
    # flip last 1 to 0 to max score
    opt2flip = score - (n - 1) + last1 + num1s - 1
 
    print(max(score, opt1flip, opt2flip))
 
    #ans = [str(x) for x in ans]
    #print(" ".join(ans))
 