# -*- coding: utf-8 -*-
'''
Created on 11/05/2016

@author: Héctor Ocampo
@author: Luis Quintero
@author: Andres Riascos
'''
'''
Clase encargada de guardar toda la informacion de tablero de juego

'''
class Tablero(object):
    Tablerito = [] # Matriz 6x8 que representa el tablero de juego, donde en las posiciones con fichas iran numeros que representen cada ficha
    Posiciones = [] # lista donde se guardara la posicion de cada ficha en el tablero, para no tener que buscar la ficha directamente en el tablero, y usar la lista como tabla hash
    FichasFinMax = [] # arreglo que guarda las fichas de max que van saliendo del juego
    FichasFinMin = [] # arreglo que guarda las fichas de min que van saliendo del juego
    Movimientos = [] # arreglo donde se guarda los movimientos que ha hecho la IA, para poder identificar el primero movimiento realizado en la expansion y mostrarlo en la pantalla
    ProMovMax = 0 # numero del proximo movimiento de max
    h = 0 # heuristica del tablero 
    
    '''
    Constructor de clase, inicializa el tablero, con su arreglo posicion con las fichas en las posiciones iniciales
    '''
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
    '''
        Crea un tablero a partir de una matriz, crea el arreglo posicion con las fichas 
        @param tablero: matriz 6x8 
        @param fichasFinMax: arreglo con las fichas de max que han salido de juego 
        @param fichasFinMin: arreglo con las fichas de min que han salido de juego 
    '''
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
    '''
    funcion que retorna la primer fila disponible en una columna especifica, retorna False si en la columna ya hay 6 fichas
    @param columna: la columna donde se verifica la disponibilidad
    @param tablero: el tablero sobre el cual se verifica
    @return: Int de la fila disponible o False si no hay fila disponible
    '''
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
            
    '''
    funcion que calcula el numero de fichas que hay en una columna, se usa para identificar el numero de movimeintos del proximo turno
    @param columna: columna donde se calculan las fichas
    @param tablerito: tablero donde se verifica las fichas
    @return: int con el numero de movimientos que tendra en el proximo turno
    '''
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
            
            
    '''
    funcion usada para determinar la profundidad del arbol, segun el numero de fichas que tenga el tablero
    @return: int con la profundidad
    '''       
    def profundidad(self):
        n = self.fichasTotales()
        r = 5
        if(n in range(15,25)): r = 5
        elif(10<=n):r = 6
        elif(1<=n):r = 7
        else: r = 4
        return r
    '''
    funcion que determina si un juego ya termino
    @return: booleano si termino o no
    '''
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