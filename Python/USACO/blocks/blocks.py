inFile = open('blocks.in', 'r')
outFile = open('blocks.out', 'w')
n = int(inFile.readline())
def retrieve(str1,str2):
    unique = str1 + str2
    over = ''
    for i in str1:
        if i in str2 and i not in over:
            over += i
    unique = unique.replace(over,'')+over
    return unique
def printResult():
    cha = ord('a')
    for _ in range(25):
        cha = chr(cha)
        outFile.write(str(alphabet[cha])+'\n')
        cha = ord(cha)
        cha += 1 
    outFile.write(str(alphabet['z']))
alphabet = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0
}
front = []
back = []
for _ in range(n):
    a =  inFile.readline().split()
    front.append(a[0])
    back.append(a[1])
for i in range(n):
    unique = retrieve(front[i],back[i])
    for char in unique:
        alphabet[char] += 1
printResult()

