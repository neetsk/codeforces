
def solve():
    a = input().split()
    b = int(a[1])
    m = int(a[2])
    a = int(a[0])
    
    print(2 + (m // b) + (m // a))


t = int(input())
for i in range(t):
    solve()