
def solve():
    n = int(input())
    s = [str(x) for x in input()]
    
    while True:
        if len(s) == 0:
            print(0)
            return
        csize = 1
        cstart = 0
        clet = s[0]
        msize = 0
        mstart = 0 
        mlet = 0
        for i in range(1, len(s)):
            if s[i] == clet:
                csize += 1
            else:
                if csize > msize:
                    msize = csize
                    mstart = cstart
                    mlet = clet
                csize = 1
                cstart = i
                clet = s[i]
        if csize > msize:
            msize = csize
            mstart = cstart
            mlet = clet
        if msize == len(s):
            print(len(s))
            return
        left = mstart
        lefts = mstart
        leftd = 0
        right = mstart + msize - 1
        rights = right
        rightd = 0
        #print(msize, mstart, mlet)  
        #scan left
        while left > 0:
            if s[left - 1] != mlet:
                left -= 1
                leftd += 1
                if leftd >= msize:
                    break
                else:
                    pass
            else:
                break
        if leftd < msize:
            # scan right
            while right < len(s) - 1:
                if s[right + 1] != mlet:
                    right += 1
                    rightd += 1
                    if leftd + rightd >= msize:
                        break
                    else:
                        pass
                else:
                    break
        #delete
        #print(left, lefts + leftd - 1, rights - rightd + 1, right)
        temp = []
        for i in range(len(s)):
            if not ((i >= left and i <= (lefts + leftd - 1)) or (i >= (rights - rightd + 1) and i <= right)):
                temp.append(s[i])
                #print(i)
        s = temp

t = int(input())
for q in range(t):
    solve()