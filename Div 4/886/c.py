
def solve():
    grid = []
    word = ""
    for i in range(8):
        grid.append(input())
    
    for i in range(8):
        for j in range(8):
            if grid[i][j] != ".":
                word += grid[i][j]
    
    print(word)
    
        

t = int(input())
for q in range(t):
    solve()
