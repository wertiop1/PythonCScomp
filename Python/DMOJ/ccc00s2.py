n = int(input())
streams = []
for i in range(n):
    streams.append(int(input()))
line = 0
while line != 77:
    line = int(input())
    if line == 99:
        stream = int(input())-1
        leftPercent = int(input())
        left = streams[stream]*leftPercent/100
        right = streams[stream] - left
        streams = streams[:stream] + [left, right] + streams[stream+1:]
    elif line == 88:
        stream = int(input()) - 1
        left = streams[stream]
        right = streams[stream + 1]
        streams = streams[:stream] + [left + right] + streams[stream+2:]
for i in range(len(streams)):
    streams[i] = str(round(streams[i]))
output = ''
for amount in streams:
    output = output + amount + ' '
output = output[:-1]
print(output)