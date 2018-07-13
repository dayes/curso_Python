#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Punto2D(object):
        """La clase facilita la operaciones con Puntos2d"""

        def __init__(self, x=0, y=0):
                """Constructor de Punto2D"""
                self.__x = x
                self.__y = y

        def __str__(self):
                """Convertir a texto"""
                return "(" + str(self.__x) + ", " + str(self.__y)+")"

        def __add__(self, p):
                """Sumar dos Puntos"""
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

