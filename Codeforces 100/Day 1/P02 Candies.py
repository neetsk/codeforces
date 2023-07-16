numK = int(input())

candy = input().split(" ")
candy = [int(x) for x in candy]

l = input().split(" ")
r = int(l[1])
l = int(l[0])

sum = 0
for i in range(l, r+1):
    sum += candy[i]

print(sum)