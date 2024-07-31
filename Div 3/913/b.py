from collections import deque

def solve():
    lower = deque()
    cap = deque()
    s = input()
    for i in range(len(s)):
        if s[i].isupper():
            if s[i] == 'B':
                if len(cap) > 0:
                    cap.pop()
            else:
                cap.append([i, s[i]])
        else:
            if s[i] == 'b':
                if len(lower) > 0:
                    lower.pop()
            else:
                lower.append([i, s[i]])
    #print(lower, cap)
    
    b = []
    l = ""
    if len(lower) > 0:
        l = lower.popleft()
    c = ""
    if len(cap) > 0:
            c = cap.popleft()
    while l != "" or c != "":
        if l == "":
            b.append(c[1])
            if len(cap) > 0:
                c = cap.popleft()
            else:
                c = ""
        elif c == "":
            b.append(l[1])
            if len(lower) > 0:
                l = lower.popleft()
            else:
                l = ""
        else:
            if l[0] < c[0]:
                b.append(l[1])
                if len(lower) > 0:
                    l = lower.popleft()
                else:
                    l = ""
            else:
                b.append(c[1])
                if len(cap) > 0:
                    c = cap.popleft()
                else:
                    c = ""
    print("".join(b))


t = int(input())
for q in range(t):
    solve()