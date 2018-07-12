

def unionListas(L1,L2):
    """
    Funcion que realice la unión de dos Listas
    """
    return set(L1) | set(L2)

def insercionListas(L1,L2):
    """
    FGuncion de intersercion de dos listas
    """
    return set(L1) & set(L2)

if __name__ == "__main__":
    L1 = ["a","b","c","d"]
    L2 = ["c", "d", "e"]
    print("La unión es: ", unionListas(L1,L2))
    print("La interssercion es: ", insercionListas(L1,L2))
