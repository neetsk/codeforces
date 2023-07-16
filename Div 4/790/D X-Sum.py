t = int(input())



for q in range(t):
    m = input().split(" ")
    n = int(m[0])
    m = int(m[1])

    grid = []

    for i in range(n):
        grid.append(input().split(" "))
        grid[i] = [int(x) for x in grid[i]]

    maxSum = 0

    for i in range(n):
        for j in range(m):
            sum = 0
            starti = i
            startj = j
            while starti > -1 and startj > -1:
                sum += grid[starti][startj]
                starti -= 1
                startj -= 1
            starti = i
            startj = j
            while starti+1 < n and startj+1 < m:
                sum += grid[starti + 1][startj + 1]
                starti += 1
                startj += 1
            starti = i
            startj = j
            while starti-1 > -1 and startj+1 < m:
                sum += grid[starti - 1][startj + 1]
                starti -= 1
                startj += 1
            starti = i
            startj = j
            while starti+1 < n and startj-1 > -1:
                sum += grid[starti + 1][startj - 1]
                starti += 1
                startj -= 1
            if sum > maxSum:
                maxSum = sum
    
    print(maxSum)
