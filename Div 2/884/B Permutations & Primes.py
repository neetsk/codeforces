import math

t = int(input())

for q in range(t):
    n = int(input())
    '''
    primes = [2] #includes up to n
    for w in range(3, n+2):
        flag = False
        for i in range(2, math.floor(math.sqrt(w)) + 1):
            if w % i == 0:
                flag = True
                break
        if not flag:
            primes.append(w)
    #found primes        
    print(primes)
    # 1 is extremely important since any subset not including 1 only has MEX() == 1
    # verify primality
    # pairs = n choose 2 + n
    
    numprimes = 0
    arr = [3, 2, 1, 4]
    for i in range(n):
        for j in range(i,n):
            flag = False
            hehe = False 
            temp = arr[i:j+1]
            for k in range(1,n+2):
                if not k in temp:
                    mex = k
                    flag = True
                    break
            if not flag:
                mex = n + 1
            if mex in primes:
                numprimes += 1
                hehe = True
            #if not mex == 1:
            print(i,j,temp,mex, hehe, sep=" ")
    print(numprimes)
    '''
    arr = [1]
    left = True
    for i in range(2, n+1):
        if i % 2 == 0 and left:
            arr = [i] + arr
            left = False
        elif i % 2 == 0 and not left:
            arr.append(i)
            left = True

    left = True
    for i in reversed(range(2, n+1)):
        if i % 2 == 1 and left:
            arr = [i] + arr
            left = False
        elif i % 2 == 1 and not left:
            arr.append(i)
            left = True
    
    print(" ".join(str(x) for x in arr))
    
                


        
                

        
        





        
