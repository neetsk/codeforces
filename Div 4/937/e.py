import math

def main():
    n = int(input())
    s = input()
    h = {}
    for i in range(n):
        if not s[i] in h:
            h[s[i]] = 1
        else:
            h[s[i]] += 1
    m = 0
    u = 0
    for k, v in h.items():
        if v > m:
            m = v
        u += 1
    if m == n or m + 1 == n:
        print(1)
        return
    f = factors(n)
    print(n // u, f)
    for i in range(len(f)):
        if f[i] > (n // u):
            f = f[0:i]
            break
    print(n // u, f)
    if len(f) == 0 or len(f) == 1:
        print(n)
        return
    
    for i in reversed(range(len(f))):
        if slide(n, s, f[i]):
            print(n // f[i])
            return
    print(n // f[len(f) - 1])
    return

t = int(input())
for i in range(t):
    main()