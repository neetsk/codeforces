
def reverse(arr, start, end):
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

def minindex(arr, left):
    min = arr[left]
    mini = left
    for i in range(left + 1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            mini = i
    return mini

def solve():
    n = input().split()
    k = int(n[1])
    n = int(n[0])

    string = [(str(x)) for x in input()]

    index = 0
    while index < n:
        m = minindex(string, index)
        print(string, index, m)
        if m == index:
            pass
        else:
            if m % 2 != index % 2 and m < n - k:
                string = reverse(string, m - 1, m)
                m = m - 1
            while m > index:
                temp = string[m - 2]
                string[m - 2] = string[m]
                string[m] = temp
                m -= 2
        index += 1

    print(" ".join(string))
    


t = int(input())
for q in range(t):
    solve()