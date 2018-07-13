# -*- coding: cp1252 -*-

import math

class Punto2D:

        def __init__(self, x=0, y=0):
                self.__x = x
                self.__y = y

        def __str__(self):
                return "(" + str(self.__x) + ", " + str(self.__y)+")"
               

        def __add__(self, p):
                """
                >>> p1 = Punto2D(3, 4)
                >>> p2 = Punto2D(8, 8)
                >>> p3 = p1 + p2
                >>> str(p3)
                >>> '(11, 12)'
                """
                return Punto2D(self.__x+p.__x,self.__y+p.__y)
                

        def distancia(self, p):
                return math.sqrt(math.pow(self.__x-p.__x,2)+math.pow(self.__y-p.__y,2))

        def __eq__(self, p):
                return self.__x == p.__x and self.__y == p.__y
        
        def __cmp__(self, p):
                # Se basa en cmp devuelve 0, 1, -1
                r1 = cmp(self.__x, p.__x)
                r2 = cmp(self.__y, p.__y)

                return cmp(r1,r2)


def _test():
        import doctest
        doctest.testmod()

if __name__ == "__main__":
        _test()
