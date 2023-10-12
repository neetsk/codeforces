
def solve():
    arr = []
    for i in range(10):
        arr.append(input())
    score = 0

    for i in range(10):
        for j in range(10):
            if arr[i][j] == "X":
                if i == 0 or i == 9:
                    score += 1
                elif (i == 1 or i == 8) and (j > 0 and j < 9):
                    score += 2
                elif (i == 1 or i == 8) and (j == 0 or j == 9):
                    score += 1
                elif (i == 2 or i == 7) and (j > 1 and j < 8):
                    score += 3
                elif (i == 2 or i == 7) and (j == 1 or j == 8):
                    score += 2
                elif (i == 2 or i == 7) and (j == 0 or j == 9):
                    score += 1
                elif (i == 3 or i == 6) and (j > 2 and j < 7):
                    score += 4
                elif (i == 3 or i == 6) and (j == 2 or j == 7):
                    score += 3
                elif (i == 3 or i == 6) and (j == 1 or j == 8):
                    score += 2
                elif (i == 3 or i == 6) and (j == 0 or j == 9):
                    score += 1
                elif (i == 4 or i == 5) and (j == 4 or j == 5):
                    score += 5
                elif (i == 4 or i == 5) and (j == 3 or j == 6):
                    score += 4
                elif (i == 4 or i == 5) and (j == 2 or j == 7):
                    score += 3
                elif (i == 4 or i == 5) and (j == 1 or j == 8):
                    score += 2
                elif (i == 4 or i == 5) and (j == 0 or j == 9):
                    score += 1
    print(score)

t = int(input())
for q in range(t):
    solve()

'''
.X........
.X........
.X........
.X........
.X........
.X........
.X........
.X........
.X........
.X........
'''