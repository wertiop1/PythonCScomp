#abcdefg
#cdefgab
composition = input()
scale = 0
for i in range(len(composition)):
    if i == 0 or composition[i-1] == '|':
        if composition[i] in 'ADE':
            scale = scale - 1
        if composition[i] in 'CFG':
            scale = scale + 1
if scale == 0:
    if composition[-1] == 'C':
        scale = scale + 1
    else:
        scale = scale - 1
if scale > 0:
    print("C-dur")
elif scale < 0:
    print("A-mol")
        
