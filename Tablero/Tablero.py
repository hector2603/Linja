'''
Created on 11/05/2016

@author: Hector Ocampo
'''
import copy

class Tablero(object):
    Tablerito = 0
    Posiciones = 0
    FichasFinMax = []
    FichasFinMin = []
    Movimientos = []
    ProMovMax = 0 # proximo movimiento de max
    h = 0 # heuristica del tablero 
    
    def __init__(self):
        self.Tablerito = [[13,1,2,3,4,5,6,7],[14,0,0,0,0,0,0,8],[15,0,0,0,0,0,0,9],[16,0,0,0,0,0,0,10],[17,0,0,0,0,0,0,11],[18,19,20,21,22,23,24,12]]
        self.Posiciones = [[0,0],]*24
        self.Movimientos = []
        i,j = 0,0
        for row in self.Tablerito:
            j=0
            for n in row:
                if (n != 0):
                    self.Posiciones[n-1]=[i,j]
                j = j+1
            i = i+1
            
    def inicialTablero(self,tablero, fichasFinMax, fichasFinMin):
        self.Tablerito = tablero
        self.Posiciones = [[0,0],]*24
        self.Movimientos = []
        self.FichasFinMax = fichasFinMax
        self.FichasFinMin = fichasFinMin
        i,j = 0,0
        for row in self.Tablerito:
            j=0
            for n in row:
                if (n != 0):
                    self.Posiciones[n-1]=[i,j]
                j = j+1
            i = i+1
        for i in range(len(fichasFinMax)):
            self.Posiciones[fichasFinMax[i]-1]="Fin"
        for i in range(len(fichasFinMin)):
            self.Posiciones[fichasFinMin[i]-1]="Fin"
        
    def posicionColumna(self, columna, tablero):
        resultado = False
        contador = 0
        if(columna>=0 and columna <= 7):
            for row in tablero:
                if (row[columna]== 0):
                    resultado = contador;
                    break
                contador = contador + 1
        return resultado
            
            
    def numeroFichasColumna(self, columna,tablerito):
        contador = 0
        for row in tablerito:
            if(row[columna] != 0):
                contador = contador +1 
        return contador-1
    
    def fichasTotales(self):
        n = 0
        for row in self.Tablerito:
            for i in row:
                if(i!=0):
                    n = n+1
        return n
            
            
            
    def profundidad(self):
        n = self.fichasTotales()
        r = 6
        if(n in range(15,25)): r = 5
        elif(10<=n):r = 6
        elif(1<=n):r = 7
        else: r = 4
        return r
    
    def termmino(self):
        contador1 = 0
        contador2 = 0
        for i in range(0,8):
            for j in range(0,6):
                if(self.Tablerito[j][i]in range(1,13)):
                    contador1 = contador1 + 1
                elif(self.Tablerito[j][i]in range(13,25)):
                    contador2 = contador2 + 1
            if((contador1+len(self.FichasFinMax)) == 12):
                break
        if((contador1+len(self.FichasFinMax)) and contador2==0):
            return True
        else:
            return False