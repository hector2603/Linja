'''
Created on 11/05/2016

@author: Hector Ocampo
'''
import copy

class Tablero(object):
    __Tablerito = 0
    __Posiciones = 0
    __FichasFinMax = []
    __FichasFinMin = []
    
    def __init__(self):
        self.__Tablerito = [[13,1,2,3,4,5,6,7],[14,0,0,0,0,0,0,8],[15,0,0,0,0,0,0,9],[16,0,0,0,0,0,0,10],[17,0,0,0,0,0,0,11],[18,19,20,21,22,23,24,12]]
        self.__Posiciones = [[0,0],]*24
        i,j = 0,0
        for row in self.__Tablerito:
            j=0
            for n in row:
                if (n != 0):
                    self.__Posiciones[n-1]=[i,j]
                j = j+1
            i = i+1
             
    def expandir(self):
        #auxTablerito,auxPos,auxFila = 0;
        for i in range(0,12):
            auxTablerito = copy.deepcopy(self.__Tablerito)
            auxPos = copy.deepcopy(self.__Posiciones)
            auxFila = 0
            auxFinMax = copy.deepcopy(self.__FichasFinMax)
            if (auxPos[i]!= "Fin") :
                auxFila = self.posicionColumna((auxPos[i][1])-1,auxTablerito)
                if(auxPos[i][1]-1 == 0):
                    auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                    auxFinMax.append(i+1) 
                    auxPos[i] = "Fin"
                elif((auxPos[i][1])>0 and auxFila != False):
                    #print "cambio valor, valor a cambiar es: "
                    #print auxTablerito[auxPos[i][0]][auxPos[i][1]]
                    auxTablerito[auxFila][auxPos[i][1]-1]= i+1
                    auxTablerito[auxPos[i][0]][auxPos[i][1]]= 0
                    auxPos[i][1] = auxPos[i][1]-1
                    auxPos[i][0] = auxFila 
                for j in range(0,12):
                    if (auxPos[i]!= "Fin") :
                        aux2Tablerito = copy.deepcopy(auxTablerito)
                        aux2Pos = copy.deepcopy(auxPos)
                        aux2FinMax = copy.deepcopy(auxFinMax)
                        auxFila = self.posicionColumna((aux2Pos[j][1])-1,aux2Tablerito)
                        if(aux2Pos[j][1]-1 == 0):
                            aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                            aux2FinMax.append(j+1) 
                            aux2Pos[j] = "Fin"
                        elif((aux2Pos[j][1])>0 and auxFila != False):
                            #print "cambio valor, valor a cambiar es: "
                            #print auxTablerito[auxPos[i][0]][auxPos[i][1]]
                            aux2Tablerito[auxFila][aux2Pos[j][1]-1]= j+1
                            aux2Tablerito[aux2Pos[j][0]][aux2Pos[j][1]]= 0
                            aux2Pos[j][1] = aux2Pos[j][1]-1
                            aux2Pos[j][0] = auxFila 
                        for row in aux2Tablerito:
                            print row
                        #self.__Tablerito = copy.deepcopy(aux2Tablerito)
                        #self.__Posiciones = copy.deepcopy(aux2Pos)
                        #self.__FichasFinMax == copy.deepcopy(aux2FinMax)
                        print aux2Pos
                        print "fichas fin"
                        print auxFinMax
        print self.__Tablerito
    
    def posicionColumna(self, columna, tablerito):
        resultado = False
        contador = 0
        for row in tablerito:
            if (row[columna]== 0):
                resultado = contador;
                break
            contador = contador + 1
        return resultado
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            