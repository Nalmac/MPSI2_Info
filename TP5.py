from random import randint

def fusionner(L1 : list[int], L2 : list[int]):
    #On détermine la liste la plus grande
    bigger_list = L1 if len(L1) >= len(L2) else L2
    smaller_list = L2 if len(L1) >= len(L2) else L1

    #On regarde chaque élement de la plus petite liste
    for e in smaller_list:
        i = 0
        #On cherche un élement plus grand dans la grand liste
        while bigger_list[i] < e:
            #Si on n'en trouve pas (dans toute la liste), on le met à la fin
            if i == len(bigger_list) -1:
                bigger_list.append(e)
                break
            else:
                i+=1
        #Si on a trouvé un élement dans la liste plus grand que e, on insère e avant cet élement
        if bigger_list[-1] != e:
            bigger_list.insert(i, e)      
    return bigger_list
        

def triFusion(L : list[int]):
    if len(L) <= 1:
        return L
    m = len(L)//2
    return fusionner(triFusion(L[:m]), triFusion(L[m:]))

def main():
    L = [randint(0, 20) for _ in range(20)]
    print(triFusion(L))

if __name__ == '__main__':
    main()