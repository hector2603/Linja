'''
Created on 16/05/2016

@author: Hector Ocampo
'''
from Tablero.Tablero import Tablero
import copy
from IA.Heuristica import Heuristica
from __builtin__ import True

class Busqueda(object):
    Tablerito = 0
    h = 0
    contador = 0;
    profundidaMax = 0


    def __init__(self, tablero):
        self.Tablerito = tablero
        self.h = Heuristica()
        self.profundidaMax = tablero.profundidad()
        
    '''    
    def expandir(self,Tablerito,profundidad,alpha,betta,jugardorMax):
        podar = False
        if(profundidad == 3):
            return Tablerito
        elif(jugardorMax):        
            for i in range(0,12):# Primer for para expandir el primer turno de MAX
                # variables auxiliares para expandir
                auxTablerito = copy.deepcopy(Tablerito.Tablerito)
                auxPos = copy.deepcopy(Tablerito.Posiciones)
                auxMovimientos = copy.deepcopy(Tablerito.Movimientos)
                auxFila = 0
                auxFinMax = copy.deepcopy(Tablerito.FichasFinMax)
                contadorMo = 0
                # fin de declaracion de variables auxiliares 
                if (auxPos[i]!= "Fin") :# si la posicion de ficha noes Fin, se va a expandir, ya que tiene mas posiciones por mover 
                    auxFila = self.Tablerito.posicionColumna((auxPos[i][1])-1,auxTablerito)# determina el numero de la fila en donde ira posicionada la ficha en la nueva posicion, retorna false si la columna ya tiene 6 fichas
                    if(auxPos[i][1]-1 <= 0): # verifica que la siguiente posicion sea la ultima
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxFinMax.append(i+1) 
                        auxPos[i] = "Fin"
                        contadorMo = 1;
                        auxMovimientos = auxMovimientos + "primer movimiento max: ficha: "+ str(i+1) +" fila: "+ str(0) +" columna: fin " 
                    elif((auxPos[i][1])>0 and (auxFila != False or isinstance( auxFila, int ) )):# para los otros casos en que la columa no tenga el  maxima de fichas 
                        auxTablerito[auxFila][auxPos[i][1]-1]= i+1
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxPos[i][1] = auxPos[i][1]-1
                        auxPos[i][0] = auxFila
                        auxMovimientos = auxMovimientos + "primer movimiento max: ficha: "+str(i+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[i][1])+" "
                        contadorMo = self.Tablerito.numeroFichasColumna(auxPos[i][1],auxTablerito) 
                        # Contar el numero de fichas en la columna para sumar -- por hacer --
                    for j in range(0,12):
                        aux2Tablerito = copy.deepcopy(auxTablerito)
                        aux2Pos = copy.deepcopy(auxPos)
                        aux2FinMax = copy.deepcopy(auxFinMax)
                        aux2Movimientos = copy.deepcopy(auxMovimientos)
                        if (auxPos[j]!= "Fin") :# creo que debo cambiar esto 
                            auxFila = self.Tablerito.posicionColumna((aux2Pos[j][1])-contadorMo,aux2Tablerito)
                            if(aux2Pos[j][1]-contadorMo <= 0):
                                aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                                aux2FinMax.append(j+1) 
                                aux2Pos[j] = "Fin"
                                aux2Movimientos = aux2Movimientos + "sdo movimiento max: ficha: "+str(j+1)+" fila: "+str(0)+" columna: fin " 
                            #elif((aux2Pos[j][1])>0 and auxFila != False):
                            else:
                                aux2Tablerito[auxFila][aux2Pos[j][1]-contadorMo]= j+1
                                aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                                aux2Pos[j][1] = aux2Pos[j][1]-contadorMo
                                aux2Pos[j][0] = auxFila
                                aux2Movimientos = aux2Movimientos + "sdo movimiento max: ficha: "+str(j+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[j][1])
                        #print("fichas 1 ",auxPos)
                        #print("fichas 2 ",aux2Pos)
                        tableroMax = Tablero()
                        tableroMax.Tablerito = aux2Tablerito
                        tableroMax.Posiciones = aux2Pos
                        tableroMax.FichasFinMax = aux2FinMax
                        tableroMax.Movimientos = aux2Movimientos
                        tableroMin = 0;
                        self.contador = self.contador +1
                        tableroMin = self.expandir(tableroMax, profundidad+1, alpha, betta, False)
                        
                        if(self.h.h(alpha)<self.h.h(tableroMin) ):
                            alpha = copy.deepcopy(tableroMax)
                            
                        if(self.h.h(betta)<=self.h.h(alpha)):
                            podar=True
                if(podar):
                    break
            return alpha;
        else:
            for i in range(12,24):# Primer for para expandir el primer turno de MAX
                # variables auxiliares para expandir
                auxTablerito = copy.deepcopy(Tablerito.Tablerito)
                auxPos = copy.deepcopy(Tablerito.Posiciones)
                auxFila = 0
                auxMovimientos = copy.deepcopy(Tablerito.Movimientos)
                auxFinMin = copy.deepcopy(Tablerito.FichasFinMin)
                contadorMo = 0
                # fin de declaracion de variables auxiliares 
                if (auxPos[i]!= "Fin") :# si la posicion de ficha noes Fin, se va a expandir, ya que tiene mas posiciones por mover 
                    auxFila = self.Tablerito.posicionColumna((auxPos[i][1])+1,auxTablerito)# determina el numero de la fila en donde ira posicionada la ficha en la nueva posicion, retorna false si la columna ya tiene 6 fichas
                    if(auxPos[i][1]+1 >= 7): # verifica que la siguiente posicion sea la ultima
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxFinMin.append(i+1) 
                        auxPos[i] = "Fin"
                        contadorMo = 1;
                        auxMovimientos = auxMovimientos + "primer movimiento min: ficha: "+str(i+1)+" fila: "+str(0)+" columna: fin" 
                    else:# para los otros casos en que la columa no tenga el  maxima de fichas 
                        auxTablerito[auxFila][auxPos[i][1]+1]= i+1
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxPos[i][1] = auxPos[i][1]+1
                        auxPos[i][0] = auxFila
                        auxMovimientos = auxMovimientos + "primer movimiento min: ficha: "+str(i+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[i][1])
                        contadorMo = self.Tablerito.numeroFichasColumna(auxPos[i][1],auxTablerito) 
                        # Contar el numero de fichas en la columna para sumar -- por hacer --
                    for j in range(12,24):
                        aux2Tablerito = copy.deepcopy(auxTablerito)
                        aux2Pos = copy.deepcopy(auxPos)
                        aux2FinMin = copy.deepcopy(auxFinMin)
                        aux2Movimientos = copy.deepcopy(auxMovimientos)
                        if (auxPos[j]!= "Fin") :# creo que debo cambiar esto 
                            auxFila = self.Tablerito.posicionColumna((aux2Pos[j][1])+contadorMo,aux2Tablerito)
                            if(aux2Pos[j][1]+contadorMo >= 7):
                                aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                                aux2FinMin.append(j+1) 
                                aux2Pos[j] = "Fin"
                                aux2Movimientos = aux2Movimientos + "sdo movimiento min: ficha: "+str(j+1)+" fila: "+str(0)+" columna: fin" 
                            #elif((aux2Pos[j][1])>0 and auxFila != False):
                            else:
                                aux2Tablerito[auxFila][aux2Pos[j][1]+contadorMo]= j+1
                                aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                                aux2Pos[j][1] = aux2Pos[j][1]+contadorMo
                                aux2Pos[j][0] = auxFila
                                aux2Movimientos = aux2Movimientos + "sdo movimiento min: ficha: "+str(j+1)+" fila: "+str(auxFila)+" columna: "+ str(aux2Pos[j][1])
                        tableroMin = Tablero()
                        tableroMin.Tablerito = aux2Tablerito
                        tableroMin.Posiciones = aux2Pos
                        tableroMin.FichasFinMin = aux2FinMin
                        tableroMin.Movimientos = aux2Movimientos
                        self.contador = self.contador +1
                        tableroMax = 0;
                        tableroMax = self.expandir(tableroMin, profundidad+1, alpha, betta, True)

                        if(self.h.h(betta)>self.h.h(tableroMax)):
                            betta = copy.deepcopy(tableroMax)
                            
                        if(self.h.h(betta)<=self.h.h(alpha)):
                            podar=True
                if(podar):
                    break
        return betta        
        '''
        
    
    def expandir(self,Tablerito,profundidad,alpha,betta,jugardorMax,movMax,movMin):
        if(profundidad == self.profundidaMax or Tablerito.termmino()):
            self.h.h(Tablerito)
            return Tablerito
        elif(jugardorMax):        
            tableroMax = Tablero()
            for i in range(0,12):# Primer for para expandir el primer turno de MAX
                # variables auxiliares para expandir
                auxTablerito = copy.deepcopy(Tablerito.Tablerito)
                auxPos = copy.deepcopy(Tablerito.Posiciones)
                auxMovimientos = copy.deepcopy(Tablerito.Movimientos)
                auxFila = 0
                auxFinMax = copy.deepcopy(Tablerito.FichasFinMax)
                movAuxMax = movMax
                # fin de declaracion de variables auxiliares 
                if (auxPos[i]!= "Fin") :# si la posicion de ficha noes Fin, se va a expandir, ya que tiene mas posiciones por mover
                    auxFila = self.Tablerito.posicionColumna((auxPos[i][1])-movAuxMax,auxTablerito)# determina el numero de la fila en donde ira posicionada la ficha en la nueva posicion, retorna false si la columna ya tiene 6 fichas
                    if(auxPos[i][1]-movAuxMax <= 0): # verifica que la siguiente posicion sea la ultima
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxFinMax.append(i+1) 
                        auxPos[i] = "Fin"
                        movAuxMax = 1;
                        auxMovimientos.append([i,0,0])
                        #auxMovimientos = auxMovimientos + "primer movimiento max: ficha: "+ str(i+1) +" fila: "+ str(0) +" columna: fin " + " profundidad: "+str(profundidad)
                    elif((auxPos[i][1])>0 and (auxFila != False or isinstance( auxFila, int ) )):# para los otros casos en que la columa no tenga el  maxima de fichas
                        auxTablerito[auxFila][auxPos[i][1]-movAuxMax]= i+1
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxPos[i][1] = auxPos[i][1]-movAuxMax
                        auxPos[i][0] = auxFila
                        auxMovimientos.append([i,auxFila,auxPos[i][1]])
                        #auxMovimientos = auxMovimientos + "primer movimiento max: ficha: "+str(i+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[i][1])+" "+ " profundidad: "+str(profundidad)
                        movAuxMax = self.Tablerito.numeroFichasColumna(auxPos[i][1],auxTablerito)
                        if(movAuxMax==0):
                            movAuxMax = 1             
                    tableroMax.Tablerito = auxTablerito
                    tableroMax.Posiciones = auxPos
                    tableroMax.FichasFinMax = auxFinMax
                    tableroMax.ProMovMax  = movAuxMax
                    tableroMax.Movimientos = auxMovimientos
                    tableroMin = 0;
                    self.contador = self.contador +1

                    tableroMin = self.expandir(tableroMax, profundidad+1, alpha, betta, False, movAuxMax, movMin)
                    if(alpha.h<tableroMin.h ):
                        alpha = copy.deepcopy(tableroMin)
                        
                    if(betta.h<=alpha.h):
                        break
            return alpha;
        else:
            for i in range(12,24):# Primer for para expandir el primer turno de MAX
                # variables auxiliares para expandir
                auxTablerito = copy.deepcopy(Tablerito.Tablerito)
                auxPos = copy.deepcopy(Tablerito.Posiciones)
                auxFila = 0
                auxMovimientos = copy.deepcopy(Tablerito.Movimientos)
                auxFinMin = copy.deepcopy(Tablerito.FichasFinMin)
                movAuxMin = movMin
                # fin de declaracion de variables auxiliares 
                if (auxPos[i]!= "Fin") :# si la posicion de ficha noes Fin, se va a expandir, ya que tiene mas posiciones por mover 
                    auxFila = self.Tablerito.posicionColumna((auxPos[i][1])+movAuxMin,auxTablerito)# determina el numero de la fila en donde ira posicionada la ficha en la nueva posicion, retorna false si la columna ya tiene 6 fichas
                    if(auxPos[i][1]+movAuxMin >= 7): # verifica que la siguiente posicion sea la ultima
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxFinMin.append(i+1) 
                        auxPos[i] = "Fin"
                        movAuxMin = 1;
                        #auxMovimientos = auxMovimientos + "primer movimiento min: ficha: "+str(i+1)+" fila: "+str(0)+" columna: fin" 
                    else:# para los otros casos en que la columa no tenga el  maxima de fichas 
                        auxTablerito[auxFila][auxPos[i][1]+movAuxMin]= i+1
                        auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                        auxPos[i][1] = auxPos[i][1]+movAuxMin
                        auxPos[i][0] = auxFila
                        #auxMovimientos = auxMovimientos + "primer movimiento min: ficha: "+str(i+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[i][1])
                        movAuxMin = self.Tablerito.numeroFichasColumna(auxPos[i][1],auxTablerito)
                        if(movAuxMin==0):
                            movAuxMin=1 
                        # Contar el numero de fichas en la columna para sumar -- por hacer --
                    tableroMin = Tablero()
                    tableroMin.Tablerito = auxTablerito
                    tableroMin.Posiciones = auxPos
                    tableroMin.FichasFinMin = auxFinMin
                    tableroMin.Movimientos = auxMovimientos
                    self.contador = self.contador +1
                    tableroMax = 0;
                    tableroMax = self.expandir(tableroMin, profundidad+1, alpha, betta, True, movMax, movAuxMin)
                    #print self.h.h(tableroMax)
                    if(betta.h>tableroMax.h):
                        betta = copy.deepcopy(tableroMax)
                        
                    if(betta.h<=alpha.h):
                        break;
            return betta
    

'''

    def expandir(self,Tablerito,profundidad):
        podar = False
        tableroResultado = 0;
        for i in range(0,12):# Primer for para expandir el primer turno de MAX
            # variables auxiliares para expandir
            auxTablerito = copy.deepcopy(Tablerito.Tablerito)
            auxPos = copy.deepcopy(Tablerito.Posiciones)
            auxMovimientos = copy.deepcopy(Tablerito.Movimientos)
            auxFila = 0
            auxFinMax = copy.deepcopy(Tablerito.FichasFinMax)
            contadorMo = 0
            # fin de declaracion de variables auxiliares 
            if (auxPos[i]!= "Fin") :# si la posicion de ficha noes Fin, se va a expandir, ya que tiene mas posiciones por mover 
                auxFila = self.Tablerito.posicionColumna((auxPos[i][1])-1,auxTablerito)# determina el numero de la fila en donde ira posicionada la ficha en la nueva posicion, retorna false si la columna ya tiene 6 fichas
                if(auxPos[i][1]-1 <= 0): # verifica que la siguiente posicion sea la ultima
                    auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                    auxFinMax.append(i+1) 
                    auxPos[i] = "Fin"
                    contadorMo = 1;
                    auxMovimientos = auxMovimientos + "primer movimiento max: ficha: "+ str(i+1) +" fila: "+ str(0) +" columna: fin " 
                elif((auxPos[i][1])>0 and auxFila != False):# para los otros casos en que la columa no tenga el  maxima de fichas 
                    auxTablerito[auxFila][auxPos[i][1]-1]= i+1
                    auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                    auxPos[i][1] = auxPos[i][1]-1
                    auxPos[i][0] = auxFila
                    auxMovimientos = auxMovimientos + "primer movimiento max: ficha: "+str(i+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[i][1])+" "
                    contadorMo = self.Tablerito.numeroFichasColumna(auxPos[i][1],auxTablerito) 
                    # Contar el numero de fichas en la columna para sumar -- por hacer --
                for j in range(0,12):
                    aux2Tablerito = copy.deepcopy(auxTablerito)
                    aux2Pos = copy.deepcopy(auxPos)
                    aux2FinMax = copy.deepcopy(auxFinMax)
                    aux2Movimientos = copy.deepcopy(auxMovimientos)
                    if (auxPos[j]!= "Fin") :# creo que debo cambiar esto 
                        auxFila = self.Tablerito.posicionColumna((aux2Pos[j][1])-contadorMo,aux2Tablerito)
                        if(aux2Pos[j][1]-contadorMo <= 0):
                            aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                            aux2FinMax.append(j+1) 
                            aux2Pos[j] = "Fin"
                            aux2Movimientos = aux2Movimientos + "sdo movimiento max: ficha: "+str(j+1)+" fila: "+str(0)+" columna: fin " 
                        #elif((aux2Pos[j][1])>0 and auxFila != False):
                        else:
                            aux2Tablerito[auxFila][aux2Pos[j][1]-contadorMo]= j+1
                            aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                            aux2Pos[j][1] = aux2Pos[j][1]-contadorMo
                            aux2Pos[j][0] = auxFila
                            aux2Movimientos = aux2Movimientos + "sdo movimiento max: ficha: "+str(j+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[j][1])

                    print("fichas 1 ",auxPos)
                    print("fichas 2 ",aux2Pos)
                    tableroMax = Tablero()
                    tableroMax.Tablerito = aux2Tablerito
                    tableroMax.Posiciones = aux2Pos
                    tableroMax.FichasFinMax = aux2FinMax
                    tableroMax.Movimientos = aux2Movimientos
                    tableroMin = 0;
                    self.contador = self.contador +1
                    expandir = False
                    if(profundidad==5):
                        tableroResultado = copy.deepcopy(tableroMax)
                        podar=True
                        print "entro a profundidad max"
                    else:
                        print "entro a else profundidad max"
                        tableroMin = self.expandirMin(tableroMax,profundidad+1)
                        expandir = True 
                    if(expandir and self.h.h(tableroMax)>self.h.h(tableroMin) ):
                        tableroResultado = copy.deepcopy(tableroMax)
                        expandir = False
                    elif(expandir and self.h.h(tableroMax)<=self.h.h(tableroMin) ):
                        tableroResultado = copy.deepcopy(tableroMin)
                        expandir = False
                    if(self.h.h(Tablerito)<=self.h.h(tableroResultado)):
                        podar=True
                        break
            if(podar):
                break
        return tableroResultado
                
         
         
    def expandirMin(self, Tablerito,profundidad):
        podar = False
        tableroResultado = 0;
        for i in range(12,24):# Primer for para expandir el primer turno de MAX
            # variables auxiliares para expandir
            auxTablerito = copy.deepcopy(Tablerito.Tablerito)
            auxPos = copy.deepcopy(Tablerito.Posiciones)
            auxFila = 0
            auxMovimientos = copy.deepcopy(Tablerito.Movimientos)
            auxFinMin = copy.deepcopy(Tablerito.FichasFinMin)
            contadorMo = 0
            # fin de declaracion de variables auxiliares 
            if (auxPos[i]!= "Fin") :# si la posicion de ficha noes Fin, se va a expandir, ya que tiene mas posiciones por mover 
                auxFila = self.Tablerito.posicionColumna((auxPos[i][1])+1,auxTablerito)# determina el numero de la fila en donde ira posicionada la ficha en la nueva posicion, retorna false si la columna ya tiene 6 fichas
                if(auxPos[i][1]+1 >= 7): # verifica que la siguiente posicion sea la ultima
                    auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                    auxFinMin.append(i+1) 
                    auxPos[i] = "Fin"
                    contadorMo = 1;
                    auxMovimientos = auxMovimientos + "primer movimiento min: ficha: "+str(i+1)+" fila: "+str(0)+" columna: fin" 
                else:# para los otros casos en que la columa no tenga el  maxima de fichas 
                    auxTablerito[auxFila][auxPos[i][1]+1]= i+1
                    auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                    auxPos[i][1] = auxPos[i][1]+1
                    auxPos[i][0] = auxFila
                    auxMovimientos = auxMovimientos + "primer movimiento min: ficha: "+str(i+1)+" fila: "+str(auxFila)+" columna: "+ str(auxPos[i][1])
                    contadorMo = self.Tablerito.numeroFichasColumna(auxPos[i][1],auxTablerito) 
                    # Contar el numero de fichas en la columna para sumar -- por hacer --
                for j in range(12,24):
                    aux2Tablerito = copy.deepcopy(auxTablerito)
                    aux2Pos = copy.deepcopy(auxPos)
                    aux2FinMin = copy.deepcopy(auxFinMin)
                    aux2Movimientos = copy.deepcopy(auxMovimientos)
                    if (auxPos[j]!= "Fin") :# creo que debo cambiar esto 
                        auxFila = self.Tablerito.posicionColumna((aux2Pos[j][1])+contadorMo,aux2Tablerito)
                        if(aux2Pos[j][1]+contadorMo >= 7):
                            aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                            aux2FinMin.append(j+1) 
                            aux2Pos[j] = "Fin"
                            aux2Movimientos = aux2Movimientos + "sdo movimiento min: ficha: "+str(j+1)+" fila: "+str(0)+" columna: fin" 
                        #elif((aux2Pos[j][1])>0 and auxFila != False):
                        else:
                            aux2Tablerito[auxFila][aux2Pos[j][1]+contadorMo]= j+1
                            aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                            aux2Pos[j][1] = aux2Pos[j][1]+contadorMo
                            aux2Pos[j][0] = auxFila
                            aux2Movimientos = aux2Movimientos + "sdo movimiento min: ficha: "+str(j+1)+" fila: "+str(auxFila)+" columna: "+ str(aux2Pos[j][1])
                    tableroMin = Tablero()
                    tableroMin.Tablerito = aux2Tablerito
                    tableroMin.Posiciones = aux2Pos
                    tableroMin.FichasFinMax = aux2FinMin
                    tableroMin.Movimientos = aux2Movimientos
                    self.contador = self.contador +1
                    tableroMax = 0;
                    expandir = False
                    if(profundidad==5):
                        tableroResultado = copy.deepcopy(tableroMin)
                        podar=True
                        print "entro a profundidad min"
                    else:
                        print "entro a else profundidad min"
                        tableroMax = self.expandir(tableroMin,profundidad+1)
                        expandir = True 
                    if(expandir and self.h.h(tableroMax)<self.h.h(tableroMin) ):
                        tableroResultado = copy.deepcopy(tableroMax)
                    elif(expandir and self.h.h(tableroMax)>=self.h.h(tableroMin) ):
                        tableroResultado = copy.deepcopy(tableroMin)
                    if(self.h.h(Tablerito)<=self.h.h(tableroResultado)):
                        podar=True
                        break
            if(podar):
                break
        return tableroResultado
        
'''