
def solve():
    s = input()
    letter = s[0]
    num = int(s[1])
    
    l = ['a','b','c','d','e','f','g','h']

    for i in range(1, num):
        print(letter + str(i))
    for i in range(num + 1, 9):
        print(letter + str(i))
    for i in range(1, 9):
        if chr(i + 96) != letter:
            print(l[i - 1] + str(num))
        

t = int(input())
for q in range(t):
    solve()