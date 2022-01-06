from random import randint

def fusionner(L1 : list[int], L2 : list[int]):
    bigger_list = L1 if len(L1) >= len(L2) else L2
    smaller_list = L2 if len(L1) >= len(L2) else L1

    for e in smaller_list:
        i = 0
        while bigger_list[i] < e:
            if i == len(bigger_list) -1:
                bigger_list.append(e)
                break
            else:
                i+=1
        if bigger_list[-1] != e:
            bigger_list.insert(i, e)      
    return bigger_list
        

def triFusion(L : list[int]):
    if len(L) <= 1:
        return L
    m = len(L)//2
    return fusionner(triFusion(L[:m]), triFusion(L[m:]))


L = [randint(0, 20) for _ in range(20)]
print(triFusion(L))