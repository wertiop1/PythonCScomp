n = int(input())
waiting = 0
late = 0 
while 1:
    if n >= 1000:
        n = 1
    service = input()
    if service == "TAKE":
        n = n+1
        waiting = waiting +1
        late = late +1
    elif service == "SERVE":
        waiting = waiting - 1
    elif service == "CLOSE":
        print(str(late)+ " " +str(waiting)+" " + str(n))
        waiting = 0 
        late = 0
    else:
        break