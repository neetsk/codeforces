
def solve():
    a = input().split()
    c = int(a[2])
    b = int(a[1])
    a = int(a[0])
    
    if a == b and b == c:
        print("YES")
        return
    
    arr = [a, b, c]
    min = 0
    minv = a
    for i in range(1, 3):
        if arr[i] < minv:
            minv = arr[i]
            min = i
    
    # never chop the min
    # see if others can equal two mins or more
    eq = 0
    v = 0
    val1 = 0
    val2 = 0
    for i in range(3):
        if arr[i] == minv:
            eq += 1
        if i != min:
            if v == 0:
                val1 = arr[i]
                v += 1
            else:
                val2 = arr[i]
            
    if eq == 1:
        if (minv * 2 == val1 and minv * 3 == val2) or (minv * 3 == val1 and minv * 2 == val2) or (minv * 2 == val1 and minv * 2 == val2):
            print("YES")
        else:
            print("NO")
    if eq == 2:
        if (max(val1, val2) / 2 == minv) or (max(val1, val2) / 3 == minv) or (max(val1, val2) / 4 == minv):
            print("YES")
        else:
            print("NO")
    #cant be 3

    
        
        

t = int(input())
for q in range(t):
    solve()