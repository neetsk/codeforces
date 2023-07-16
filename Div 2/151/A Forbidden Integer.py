t = int(input())

for q in range(t):
    b = input().split(" ")
    n = int(b[0])
    k = int(b[1])
    x = int(b[2])

    temp = ""

    if not x == 1:
        print("YES")
        print(n)
        for i in range(n):
            temp += "1 "
        print(temp[0:len(temp)])
    elif x == 1 and k == 1:
        print("NO")
    else:
        if k == 2:
            if n % 2 == 0:
                print("YES")
                print(n // 2)
                for i in range(n//2):
                    temp += ("2 ")
                print(temp[0:len(temp)])
            else:
                print("NO")
        else:
            print("YES")
            numdigits = 0
            while n - 2 > 1:
                numdigits += 1
                n = n - 2
            print(numdigits + 1)
            for i in range(numdigits):
                temp += "2 "
            temp += str(n)
            print(temp[0:len(temp)])
            

    



        
