# -*- coding: utf-8 -*-

'''
Created on 24/05/2016

@author: Héctor Ocampo
@author: Luis Quintero
@author: Andrés Riascos
'''
from Tablero.Tablero import Tablero
'''
clase encargada de decir el valor heuristico de un tablero 
'''
class Heuristica(object):
    
    Tablerito = Tablero()
    '''
    constructor
    '''
    def __init__(self):
        self.Tablerito = Tablero();
    '''
    función que calcula la heuristica del tablero
    @param tablero: Objeto tablero al cual se le calculará el valor H
    @return: int correspondiente al valor de la heuristica  
    ''' 
    def h(self,tablero):
        h = 0;
        contadorMax = 0;
        contadorMin = 0;
        for row in tablero.Tablerito:
            for n in range(1,4):
                if(row[n]<=12 and row[n]!=0):
                    if(n==3):contadorMax = contadorMax + 1
                    if(n==2):contadorMax = contadorMax + 2
                    if(n==1):contadorMax = contadorMax + 3
            for n in range(4,7):
                if(row[n]>=13):
                    if(n==4):contadorMin = contadorMin + 1
                    if(n==5):contadorMin = contadorMin + 2
                    if(n==6):contadorMin = contadorMin + 3
        contadorMax = contadorMax + len(tablero.FichasFinMax)*5
        contadorMin = contadorMin + len(tablero.FichasFinMin)*5
        h = contadorMax - contadorMin;
        tablero.h = h
        return h
            
        