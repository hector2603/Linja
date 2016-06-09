'''
Created on 11/05/2016

@author: Hector Ocampo
'''
from Tablero.Tablero import Tablero
from IA.Busqueda import Busqueda
from IA.Heuristica import Heuristica


if __name__ == '__main__':

    tablerito = Tablero()
    tableritoNegativo = Tablero();
    tableritoPositivo = Tablero();
    tableritoNegativo.FichasFinMin = [0,]*100
    tableritoPositivo.FichasFinMax = [0,]*100
    h = Heuristica()
    h.h(tableritoNegativo)
    h.h(tableritoPositivo)

    print tablerito.fichasTotales()
    print tablerito.profundidad()
    print tablerito.termmino()
    #tablerito.Tablerito = [[0,0,0,0,0,0,0,0],]*8
    #tablerito.FichasFinMax = [0,]*12
    print tablerito.termmino()
    for row in tablerito.Tablerito:
        print row
    
    jugar = True
    movMin = 1
    movMax = 1
    while jugar:
        auxPos = tablerito.Posiciones
        auxTablerito = tablerito.Tablerito
        auxFinMin = tablerito.FichasFinMin
        auxFinMax = tablerito.FichasFinMax
        tablerito.Movimientos = []
        print"Tu turno"
        f = int(input("ingrese el numero de la ficha a mover:"))
        if (tablerito.Posiciones[f-1]!= "Fin") :# si la posicion de ficha noes Fin, se va a expandir, ya que tiene mas posiciones por mover 
            auxFila = tablerito.posicionColumna((auxPos[f-1][1])+movMin,tablerito.Tablerito)# determina el numero de la fila en donde ira posicionada la ficha en la nueva posicion, retorna false si la columna ya tiene 6 fichas
            if(auxPos[f-1][1]+movMin >= 7): # verifica que la siguiente posicion sea la ultima
                auxTablerito[auxPos[f-1][0]][auxPos[f-1][1]]= 0
                auxFinMin.append(f) 
                auxPos[f-1] = "Fin"
                movMin = 1;
            else:# para los otros casos en que la columa no tenga el  maxima de fichas 
                auxTablerito[auxFila][auxPos[f-1][1]+movMin]= f
                auxTablerito[auxPos[f-1][0]][auxPos[f-1][1]]= 0
                auxPos[f-1][1] = auxPos[f-1][1]+movMin
                auxPos[f-1][0] = auxFila
                movMin = tablerito.numeroFichasColumna(auxPos[f-1][1],auxTablerito)
                if(movMin==0):
                    movMin=1 
                # Contar el numero de fichas en la columna para sumar -- por hacer --
        for row in tablerito.Tablerito:
            print row
        print movMin
        if(tablerito.termmino()):
            break
        print "turno maquina"
        #LLamado a la expansion del tablero
        buscador = Busqueda(tablerito)
        tableritoResultado =  buscador.expandir(tablerito,0,tableritoNegativo,tableritoPositivo,True,movMax,movMin) #en la varibale tablerito Resultado se guarda la decision minimax
        #Fin del llamado
        print "Nodos creados"
        print buscador.contador
        
        posicionMovimiento = tableritoResultado.Movimientos[0] ##en posicion movimiento se guarda la ficha y las cordenadas de la ficha que se va a mover en ese turno
        print auxPos[posicionMovimiento[0]]
        #Inicio del cambio de posiciones  
        if(posicionMovimiento[2]==0): 
            auxTablerito[auxPos[posicionMovimiento[0]][0]][auxPos[posicionMovimiento[0]][1]]= 0
            auxFinMin.append(posicionMovimiento[0])
            auxFinMax.append(posicionMovimiento[0]+1) 
            auxPos[posicionMovimiento[0]] = "Fin"
            movMax = 1;
        else:
            auxTablerito[posicionMovimiento[1]][posicionMovimiento[2]]= posicionMovimiento[0]+1
            auxTablerito[auxPos[posicionMovimiento[0]][0]][auxPos[posicionMovimiento[0]][1]]= 0
            auxPos[posicionMovimiento[0]][0] = posicionMovimiento[1]
            auxPos[posicionMovimiento[0]][1] = posicionMovimiento[2]
            movMax = tablerito.numeroFichasColumna(auxPos[posicionMovimiento[0]][1],auxTablerito)
            if(movMax==0):
                movMax=1
        print posicionMovimiento
        print "movimientos del proximo turno "+str(movMax)
        for row in tablerito.Tablerito:
            print row
        print auxPos
        #En caso de que el movimiento hecho por max termine el juego
        if(tablerito.termmino()):
            break;
    
    #decide quien gana
    if(h.h(tablerito)>0):
        print "gano la IA"
    else:
        print "ganaste"
    '''
    print "contador"
    print buscador.contador
    print "heuristica"
    print h.h(resultado)
    print resultado.Posiciones
    print resultado.FichasFinMax
    print resultado.FichasFinMin
    print resultado.Movimientos'''