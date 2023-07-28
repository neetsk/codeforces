t = int(input())

for q in range(t):
    n = int(input())

    skilla = float('inf')
    skillb = float('inf')
    skillab = float('inf')

    for i in range(n):
        minutes, skills = input().split() 
        minutes = int(minutes)

        if skills == "11":
            if minutes < skillab:
                skillab = minutes
        elif skills == "10":
            if minutes < skilla:
                skilla = minutes
        elif skills == "01":
            if minutes < skillb:
                skillb = minutes
    
    if (skilla == float('inf') or skillb == float('inf')) and skillab == float('inf'):
        print(-1)
    else:
        if skilla + skillb < skillab:
            print(skilla + skillb)
        else:
            print(skillab)
    
        



    


    