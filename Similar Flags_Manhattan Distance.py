# Finding 3 images each similar to the giving image in the CSD 64-dimensional vector. 
# Use of the Manhattan ( L1 ) distance for the distance.

flagsdata = open("flag_CSD.dat", "r")
data = flagsdata.readline()
data1 = data.split()
countOfFlags = int(data1[0])
countOfColors = int(data1[1])
flags = [ [ None for y in range(countOfColors) ] for x in range(countOfFlags) ]
targetFlags = [77,8,87,34]

for f in range(0,countOfFlags):
    #print(f)
    colorsOfFlag = flagsdata.readline()
    #print(colorsOfFlag)
    colors = colorsOfFlag.split()
    for c in range(0,countOfColors):
        #print(f,c)
        flags[f][c] = int(colors[c])

distance =  [ [ 0 for y in range(countOfFlags) ] for x in range(len(targetFlags)) ]
for i in range(0,len(targetFlags)):
    tfi = targetFlags[i]
    tf = flags[tfi - 1]
    for j in range(0,len(flags)):
        f = flags[j]
        for c in range(0,countOfColors):
            #print(tf[c], f[c])
            distance[i][j] += abs(tf[c] - f[c])


import codecs
file = codecs.open("flag_list.txt", 'r', encoding='utf8')
#flagslist = file.readline() # read just one line
#print(flagslist)
flagNames = [None for x in range(0, 200)]
while True:
    flagName = file.readline()
    if not flagName:
        break
    #print(flagName)
    x = flagName.split()
    #print(x[0], x[1], x[2])
    flagNames[int(x[0])-1] = x[1] + ": " + x[2]
    print(flagNames[int(x[0])])


#print(flagNames)
file.close()
#minL = [[999,-1],[999,-1],[999,-1],[999,-1]]
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
    #print(distance[i])

    #print(distance[i][0], distance[i][1], distance[i][2], distance[i][3])

#print(flags)

flagsdata.close()