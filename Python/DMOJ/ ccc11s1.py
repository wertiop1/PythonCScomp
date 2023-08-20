n = int(input())
s = 0
t = 0
for i in range(n):
    sentence = input()
    sentence = sentence.lower()
    s = s + sentence.count('s')
    t = t + sentence.count('t')
if t > s:
    print("English")
else:
    print("French")