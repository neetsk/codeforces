t = int(input())

for q in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(" ")]

    blank = 0
    longest = 0

    for i in range(n):
        if arr[i] == 0:
            blank += 1
            if longest < blank:
                longest = blank
        else:
            blank = 0
    
    print(longest)