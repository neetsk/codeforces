t = int(input())

for q in range(t):
    s = input()
    compare = "codeforces"
    diff = 0
    for i in range(len(compare)):
        if compare[i] != s[i]:
            diff += 1
    print(diff)