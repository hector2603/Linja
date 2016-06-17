# -*- coding: utf-8 -*-
'''
Created on 9/06/2016

@author: Héctor Ocampo
@author: Luis Quintero
@author: Andres Riascos
'''
import copy
from Tablero.Tablero import Tablero

class LectorTexto(object):
    '''
    clase encargada de abrir el archivo de texto y crear una matriz con los datos 
    '''
    Ruta = ""
    archivo = 0
    '''
    constructor de la clase
    @param ruta: recibe la ruta donde se encuentra el archivo de texto 
    '''
    def __init__(self,ruta):
        self.Ruta = ruta;
    '''
    abre el archivo de texto y lo guarda en la variable archivo 
    '''
    def abrir(self):
        self.archivo = open(self.Ruta,'r')
    '''
    dado el archivo de texto, crea la matriz con los datos, y dos arreglos con las fichas que ya terminaron el juego
    @return: retorna un objeto tablero con los datos cargados 
    '''
    def crearTablero(self):
        tablero = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        contadorFichasMax = 0
        contadorFichasMin = 12
        fichasFinMax = []
        fichasFinMin = []
        for i in range(0,6):
            linea = self.archivo.readline()
            for j in range(0,8):
                if(int(linea[j])==1):
                    contadorFichasMax = contadorFichasMax + 1
                    tablero[i][j] = contadorFichasMax
                elif(int(linea[j])==2):
                    contadorFichasMin = contadorFichasMin +1
                    tablero[i][j] = contadorFichasMin
        for i in range(contadorFichasMax+1,13):
            fichasFinMax.append(i)
        for i in range(contadorFichasMin+1,25):
            fichasFinMin.append(i)    
        Tablerito = Tablero()
        Tablerito.inicialTablero(tablero, fichasFinMax,fichasFinMin)
        return Tablerito
    '''
    funcion que cierra el archivo de texto
    '''
    def cerrar(self):
        self.archivo.close()