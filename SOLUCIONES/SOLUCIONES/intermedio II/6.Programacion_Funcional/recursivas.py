# funcion siguiente([2,5,7]) ==> [3,6,8]

def siguiente(L):
        if L==[]:
                return []
        else:
                return [L[0]+1]+siguiente(L[1:])





# Suma de los listas:
def suma(L1,L2):
        if L1==[] and L2==[]:
                return []
        elif L1==[]:
                return L2
        elif L2==[]:
                return L1
        else:
                return [L1[0]+L2[0]] + suma(L1[1:],L2[1:])


print (siguiente([2,5,7]))
print (suma([1,2,3],[4,5,6]))
print (suma([1,2,3,6,8],[4,5,6]))
