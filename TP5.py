from random import randint

def fusionner(L1 : list[int], L2 : list[int]):
    mergedList = []
    for i in range(max(len(L1), len(L2))):
        if i >= len(L1):
            mergedList.append(L2[i])
        elif i >= len(L2):
            mergedList.append(L1[i])
        else:
            mergedList += [min(L1[i], L2[i]), max(L1[i], L2[i])]
    return mergedList


