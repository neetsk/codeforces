
def main():
    a = int(input())
    arr = [0] * (2 * a)
    for i in range(2 * a):
        sym = "#"
        opp = "."
        if (i // 2) % 2 == 1:
            sym = "."
            opp = "#"
        for j in range(2 * a):
            if (j // 2) % 2 == 0:
                arr[j] = sym
            else:
                arr[j] = opp
        print(''.join(arr))
    return

t = int(input())
for i in range(t):
    main()