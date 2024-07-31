
def main():
    a = input().split()
    b = int(a[1])
    c = int(a[2])
    a = int(a[0])

    if a < b and b < c:
        print("STAIR")
        return
    if a < b and b > c:
        print("PEAK")
        return
    print("NONE")
    return
t = int(input())
for i in range(t):
    main()