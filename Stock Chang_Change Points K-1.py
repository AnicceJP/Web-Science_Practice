# Use of Greedy method in order to detect change points with the number 
# of change points K = 1. Plotting time-series data and approximate straight line.

import matplotlib.pyplot as plt
valuesdata = open("stock_value.txt", "r") #open data
i = 0
while True:
    data = valuesdata.readline()
    data1 = data.split()
    i += 1
    if i == 674:
        break

import codecs #open file with companies names
with codecs.open("stock_name_utf8.txt", "r", encoding='utf8') as ins:
    array = []
    for line in ins:
        array.append(line)
company = array[i-1]
print(company)

# finding LR
max = 0
maxt = 0
t = 0
e = int(len(data1) - 1)
ys = int(data1[t-1])
ye = int(data1[e])

maxval = 0 # for maximum value in data
minval1 = 9999 # for minimum value before LR

for t in range(t-1,e-1):
    yt = int(data1[t])
    LR = ((yt - ys) ^ 2) / (t - (t - 1)) + ((ye - yt) ^ 2) / (e - t) - ((ye - ys) ^ 2) / (e - (t - 1))
    if max < LR:
        max = LR
        maxt = t
    if maxval < yt:
        maxval = yt
    if minval1 > yt:
        minval1 = yt

def minimum(a, b): # for minimum value after LR
    return a if a < b else b
numbers = data1[maxt+1:e]
minval2 = numbers[0]
for elem in numbers:
    minval2 = minimum(minval2, elem)
minval2 = int(minval2)

#finding average value for the parts before and after LR
avg1 = (minval1 + maxval)/2
avg2 = (minval2 + maxval)/2
print('K = 1, LR =', max, ', change point =', maxt)


#building plot
x = [i for i in range(len(data1))]
y = [int(data1[i]) for i in range(len(data1))]

plt.plot(x, y, linewidth= 0.5)
plt.xlabel('Time')
plt.ylabel('Value')
plt.plot(1000, 250)
plt.grid()
plt.plot([maxt, maxt], [avg1, avg2], color= 'green', linewidth= 0.5)
plt.plot([0, maxt], [avg1, avg1], color= 'green', linewidth= 0.5)
plt.plot([maxt, e], [avg2, avg2], color= 'green', linewidth= 0.5)
plt.show()

