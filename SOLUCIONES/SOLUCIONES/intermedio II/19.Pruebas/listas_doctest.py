def moda(L):
        # calcular la moda de una lista de enteros
        """
        >>> L = [3,4,5,6,7,8,8,9,8,8,2,1,9]
        >>> moda(L)
        (8, 3)
        """
        conteo={}

        for i in L:
                if i in conteo.keys():                       
                        conteo[i]+=1
                else:
                        conteo[i]=1
        
        valor = max(conteo.values())
        elementos = list(conteo.items())

        #Con el parametro key definimos una funcion que nos indica, cual es la clave:
        elementos.sort(key=lambda x:x[1],reverse=True)
        
        return elementos[0][0], elementos[0][1]



def _test():
        import doctest
        doctest.testmod()

if __name__ == "__main__":
        _test()
