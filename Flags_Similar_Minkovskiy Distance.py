# The code for searching 3 most similar flags to each of the 4 given flags by colors
# according to the formula L1 of Minkovkiy distances:

flagsdata = open("flag_CSD.dat", "r")
data = flagsdata.readline()
data1 = data.split()
countOfFlags = int(data1[0])
countOfColors = int(data1[1])
flags = [ [ None for y in range(countOfColors) ] for x in range(countOfFlags) ]
targetFlags = [77,8,87,34]

for f in range(0,countOfFlags):
    colorsOfFlag = flagsdata.readline()
    colors = colorsOfFlag.split()
    for c in range(0,countOfColors):
        flags[f][c] = int(colors[c])

distance =  [ [ 0 for y in range(countOfFlags) ] for x in range(len(targetFlags)) ]
for i in range(0,len(targetFlags)):
    tfi = targetFlags[i]
    tf = flags[tfi - 1]
    for j in range(0,len(flags)):
        f = flags[j]
        for c in range(0,countOfColors):
            distance[i][j] += abs(tf[c] - f[c])

import codecs
file = codecs.open("flag_list.txt", 'r', encoding='utf8')
flagNames = [None for x in range(0, 200)]
while True:
    flagName = file.readline()
    if not flagName:
        break
    x = flagName.split()
    flagNames[int(x[0])-1] = x[1] + ": " + x[2]

file.close()
for i in range(0,len(distance)):
    print("the most similar flags to ", flagNames[targetFlags[i]-1])
    for k in range(0,4):
        m = 999
        n = 0
        for j in range(0,len(distance[i])):
            if distance[i][j] < m and distance[i][j] != 0:
                m = distance[i][j]
                n = j
        distance[i][n] = 999
        print(flagNames[n], m)

flagsdata.close()
