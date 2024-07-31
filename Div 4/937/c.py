
def main():
    a = input()
    am = "AM" if int(a[0:2]) < 12 else "PM"
    hour = int(a[0:2])
    minute = a[3:5]
    if hour == 0:
        hour = 12
    elif hour > 12:
        hour = hour % 12
    hour = ("0" + str(hour)) if hour < 10 else str(hour)
    print(hour + ":" + minute + " " + am)
    return

t = int(input())
for i in range(t):
    main()