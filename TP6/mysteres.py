def mystere2(L : list) -> list:
    def interne(L : list, i : int):
        if i == len(L):
            return [L.copy()]
        r = []
        for k in range(i, len(L)):
            (L[i], L[k]) = (L[k], L[i])
            r += interne(L, i+1)
            (L[i], L[k]) = (L[k], L[i])
        return r
    return interne(L, 0)

def main():
    print(mystere2(list("hello")))

if __name__ == '__main__':
    main()
