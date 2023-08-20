song = ['A', 'B', 'C', 'D', 'E']
def button1():
    song[0] = a
    song[1] = b
    song[2] = c
    song[3] = d
    song[4] = e
    song[0] = e
    song[1] = d
    song[2] = c
    song[3] = b
    song[4] = a
def button2():
    song[0] = a
    song[1] = b
    song[2] = c
    song[3] = d
    song[4] = e
    song[0] = e
    song[1] = a
    song[2] = b
    song[3] = c
    song[4] = d
def button3():
    song[0] = a
    song[1] = b
    song[0] = b
    song[1] = a
def button4():
    print(song)
while True:
    b = int(input())
    n = int(input())
    for i in range(n):
        if b == 1:
            button1
        if b == 2:
            button2
        if b == 3:
            button3
        if b==4:
            button4
            break
    