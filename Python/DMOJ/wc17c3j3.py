password = list(input())
numbers = 0
uppercase = 0
lowercase = 0
o = 0
for i in range(len(password)):
    try:
        int(password[o])
        numbers = numbers + 1
        o = o + 1
    except:
        pass
o = 0
if numbers >= 1:
    pass
else: 
    print("Invalid")
    exit()
for i in range(len(password)):
    if password[o].isupper() == True:
        uppercase = uppercase + 1
    else:
        pass
    o = o + 1
if uppercase >= 2:
    pass
else: 
    print("Invalid")
    exit()
o = 0
for i in range(len(password)):
    if password[o].islower() == True:
        lowercase = lowercase + 1
    else:
        pass
    o = o + 1
if lowercase >= 3:
    print("Valid")
else: 
    print("Invalid")
    


