from random import randint

def fusionner(L1 : list[int], L2 : list[int]):
    mergedList = L1 if len(L1) >= len(L2) else L2
    mergingList = L2 if len(L1) >= len(L2) else L1
    
    while mergingList:
        for i in range(len(mergedList)):
            for item in mergingList:
                if item <= mergedList[i]:
                    mergedList.insert(i, item)
                    mergedList.pop(i)
        if len (mergingList) == 1:
            mergedList.append(mergingList[0])
            mergingList.pop(0)

    return mergedList
    


def triFusion(L : list[int]):
    if len(L) <= 1:
        return L
    m = len(L)//2
    return fusionner(triFusion(L[:m]), triFusion(L[m:]))


L = [0, 2, 5, 9]; L2 = [3, 6, 8, 45]
print(fusionner(L, L2))