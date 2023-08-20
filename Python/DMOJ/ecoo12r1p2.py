prometer = "TATAAT"
def complementary(string):
    placeholder = ''
    for characters in string:
        if characters == "A":
            placeholder = placeholder + "T"
        elif characters == "T":
            placeholder = placeholder + "A"
        elif characters == "C":
            placeholder = placeholder + "G"
        else:
            placeholder = placeholder + "C"
    return placeholder
for dataset in range(5):
    strand = input()
    beginning = strand.index(prometer)+10
    while 1:
        varBegin = beginning
        section = strand[varBegin:varBegin+6]
        secRev = section[::-1]
        if complementary(secRev) in strand[varBegin + 6:]:
            break
        else:
            varBegin += 1
    rna = strand[beginning:varBegin]
    rna = complementary(rna)
    rna = rna.replace('T', 'U')
    print(f'{dataset+1}: {rna}')
