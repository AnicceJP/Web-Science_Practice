# Finding the best location of the third store, using Greedy method.

P1 = [2,2] #Known Store1
P2 = [5,1] #Known Store2
bestStorePosition = [-1,-1]
for i in range(1,6): #potential store3
    for j in range(1,6):
        #score for potential store3:
        MG = 0
        for m in range(1,6): #start point
            for n in range(1,6):
                distanceToPotentialStore = abs(m - i) + abs(n - j)
                distanceToKnownStore1 = abs(P1[0] - m) + abs(P1[1] - n)
                distanceToKnownStore2 = abs(P2[0] - m) + abs(P2[1] - n)
                #print("potential store: ", i, j, "person: " , m, n, "distanceToPotentialStore: ", distanceToPotentialStore, "distanceToKnownStore1: ", distanceToKnownStore1, "distanceToKnownStore2: ", distanceToKnownStore2)
                MG = MG + max(1 / (1 + distanceToPotentialStore) - 1 / (1 + distanceToKnownStore1), 0)
                MG = MG + max(1 / (1 + distanceToPotentialStore) - 1 / (1 + distanceToKnownStore2), 0)
                node = 0
                if i < 6:
                    node = (i - 1) * 5 + j
                else:
                    node = i * 5 + j
        print("potential store3 node: ", node, ", MG: ", MG)
        if MG > bestStorePosition[1]:
            bestStorePosition[0] = node
            bestStorePosition[1] = MG
    print()
print("The Best Store3 Position node: ", bestStorePosition[0], ", MG: ", bestStorePosition[1])
