'''
Created on 9/06/2016

@author: Hector Ocampo
'''
import copy
from Tablero.Tablero import Tablero

class LectorTexto(object):
    '''
    classdocs
    '''
    Ruta = ""
    archivo = 0

    def __init__(self,ruta):
        self.Ruta = ruta;

    def abrir(self):
        self.archivo = open(self.Ruta,'r')

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
        
    def cerrar(self):
        self.archivo.close()