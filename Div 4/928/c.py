
def sum(n):
    return (n * (n + 1)) // 2

def solve():
    n = int(input())
    arr = [0,0,0,0,0,0]

    if n < 10:
        print(sum(n))
        return
    arr[0] = sum(9)
    if n < 100:
        print((arr[0] * (n // 10)) + (10 * ((n // 10) - 1)) + sum((n % 10) + (n // 10)) + (n // 10))
    arr[1] = arr[0] * 10 + arr[0] * 10

    '''
    1-9
    n + n1 / 2
    10-19
    45 + n + n1 / 2
    1 - 9 = 45
    1 - 10 = 55
    2 - 11 = 65
    3 - 12 = 75
    4 - 13 = 85
    5 - 14 = 95
    6 - 15
    7 - 16
    8 - 17
    9 - 18
    ======== 100
    1 - 10
    2 - 11
    3 - 12
    ..
    9 - 18
    ======== 200
    2 - 11
    '''
t = int(input())
for i in range(t):
    solve()