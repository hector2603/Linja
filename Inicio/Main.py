'''
Created on 11/05/2016

@author: Hector Ocampo
'''
from PyQt4 import QtCore, QtGui
import sys
from Tablero.Tablero import Tablero
from IA.Busqueda import Busqueda
from IA.Heuristica import Heuristica
from Lector.LectorTexto import LectorTexto
from Interfaz import *

class ejecutarGame(QtGui.QDialog):
    
    def __init__(self, parent = None): 
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()  
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.leerArchivoDeTexto, QtCore.SIGNAL('clicked()'), self.iniciarJuego)
        QtCore.QObject.connect(self.ui.salir, QtCore.SIGNAL('clicked()'), self.salirPrograma)  
         
     
    def iniciarJuego(self):
<<<<<<< HEAD
        #Este es el lector de texto que implemente
        lector = LectorTexto("../Linja.txt")
        lector.abrir()
        tablerito = lector.crearTablero()
        lector.cerrar()      
        #tablerito = Tablero()
=======
        #con esto leemos el archivo de texto 3 lineas
        #Este es el lector de texto que implemente
        #lector = LectorTexto("../Linja.txt")
        #lector.abrir()
        #tablerito = lector.crearTablero()
        #lector.cerrar()      
        archivo = open("prueba.txt", "r") 
        for linea in archivo.readlines():
            print linea
        tablerito = Tablero()
>>>>>>> origin/master
        tableritoNegativo = Tablero();
        tableritoPositivo = Tablero();
        tableritoNegativo.FichasFinMin = [0,]*100
        tableritoPositivo.FichasFinMax = [0,]*100
        h = Heuristica()
        h.h(tableritoNegativo)
        h.h(tableritoPositivo)
    
        print "Fichas Totales "+ str(tablerito.fichasTotales())
        print "Fichas Profundidad "+ str(tablerito.profundidad())
        print "Termino? "+ str(tablerito.termmino())
        #tablerito.Tablerito = [[0,0,0,0,0,0,0,0],]*8
        #tablerito.FichasFinMax = [0,]*12
        x = 0 #x = fila y row[i] columna colorFicha
        colorFicha = "null" 
        for row in tablerito.Tablerito:           
            print row
            for i in range(0,8):
                if(row[i] >= 1 and row[i] <= 12):
                    colorFicha="roja"
                    self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])
                if(row[i] >= 13 and row[i] <= 24):
                    colorFicha="negra"
                    self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])
                if(row[i]==0):
                    colorFicha="null"
                    self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])          
            x += 1
            
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
            #f = int(input("ingrese el numero de la ficha a mover:"))
            tupla =  QtGui.QInputDialog.getInt(self, "Realizar tu Movimiento de la Ficha", "Cual Ficha Usted Desea Mover? (13 - 24)", min=13, max=24, step=1)                
            if tupla[1] == False:
                sys.exit(0)
            else:
                f = tupla[0]
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
            #for row in tablerito.Tablerito:
                #print row
            x = 0 #x = fila y row[i] columna colorFicha
            colorFicha = "null" 
            for row in tablerito.Tablerito:           
                print row
                for i in range(0,8):
                    if(row[i] >= 1 and row[i] <= 12):
                        #self.ui.b0_0.setIcon(QtGui.QIcon("Img Linja/torre_roja.png"))#con esto se dibuja en la ficha
                        colorFicha="roja"
                        self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])
                    if(row[i] >= 13 and row[i] <= 24):
                        #self.ui.b1_1.setIcon(QtGui.QIcon("Img Linja/torre_negra.png"))#con esto se dibuja en la ficha
                        colorFicha="negra"
                        self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])
                    if(row[i]==0):
                        colorFicha="null"
                        self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])            
                x += 1
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
            #for row in tablerito.Tablerito:
                #print row
            x = 0 #x = fila y row[i] columna colorFicha
            colorFicha = "null" 
            for row in tablerito.Tablerito:           
                print row
                for i in range(0,8):
                    if(row[i] >= 1 and row[i] <= 12):
                        #self.ui.b0_0.setIcon(QtGui.QIcon("Img Linja/torre_roja.png"))#con esto se dibuja en la ficha
                        colorFicha="roja"
                        self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])
                    if(row[i] >= 13 and row[i] <= 24):
                        #self.ui.b1_1.setIcon(QtGui.QIcon("Img Linja/torre_negra.png"))#con esto se dibuja en la ficha
                        colorFicha="negra"
                        self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])
                    if(row[i]==0):
                        colorFicha="null"
                        self.dibujarFichasTableroInicial(x, i, colorFicha, row[i])            
                x += 1
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
    
    def salirPrograma(self):
        sys.exit(0)
        
    def dibujarFichasTableroInicial(self, fila , columna, colorFicha, numeroFicha):
        #fila0
        if(fila==0 and columna ==0):
            self.ui.b0_0.setText(str(numeroFicha))
            self.ui.b0_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==0 and columna ==1):
            self.ui.b1_0.setText(str(numeroFicha))
            self.ui.b1_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==0 and columna ==2):
            self.ui.b2_0.setText(str(numeroFicha))
            self.ui.b2_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==0 and columna ==3):
            self.ui.b3_0.setText(str(numeroFicha))
            self.ui.b3_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==0 and columna ==4):
            self.ui.b4_0.setText(str(numeroFicha))
            self.ui.b4_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==0 and columna ==5):
            self.ui.b5_0.setText(str(numeroFicha))
            self.ui.b5_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==0 and columna ==6):
            self.ui.b6_0.setText(str(numeroFicha))
            self.ui.b6_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==0 and columna ==7):
            self.ui.b7_0.setText(str(numeroFicha))
            self.ui.b7_0.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        #fila 1
        if(fila==1 and columna ==0):
            self.ui.b0_1.setText(str(numeroFicha))
            self.ui.b0_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==1 and columna ==1):
            self.ui.b1_1.setText(str(numeroFicha))
            self.ui.b1_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==1 and columna ==2):
            self.ui.b2_1.setText(str(numeroFicha))
            self.ui.b2_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==1 and columna ==3):
            self.ui.b3_1.setText(str(numeroFicha))
            self.ui.b3_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==1 and columna ==4):
            self.ui.b4_1.setText(str(numeroFicha))
            self.ui.b4_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==1 and columna ==5):
            self.ui.b5_1.setText(str(numeroFicha))
            self.ui.b5_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==1 and columna ==6):
            self.ui.b6_1.setText(str(numeroFicha))
            self.ui.b6_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==1 and columna ==7):
            self.ui.b7_1.setText(str(numeroFicha))
            self.ui.b7_1.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        #fila 2
        if(fila==2 and columna ==0):
            self.ui.b0_2.setText(str(numeroFicha))
            self.ui.b0_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==2 and columna ==1):
            self.ui.b1_2.setText(str(numeroFicha))
            self.ui.b1_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==2 and columna ==2):
            self.ui.b2_2.setText(str(numeroFicha))
            self.ui.b2_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==2 and columna ==3):
            self.ui.b3_2.setText(str(numeroFicha))
            self.ui.b3_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==2 and columna ==4):
            self.ui.b4_2.setText(str(numeroFicha))
            self.ui.b4_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==2 and columna ==5):
            self.ui.b5_2.setText(str(numeroFicha))
            self.ui.b5_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==2 and columna ==6):
            self.ui.b6_2.setText(str(numeroFicha))
            self.ui.b6_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==2 and columna ==7):
            self.ui.b7_2.setText(str(numeroFicha))
            self.ui.b7_2.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        #fila 3
        if(fila==3 and columna ==0):
            self.ui.b0_3.setText(str(numeroFicha))
            self.ui.b0_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==3 and columna ==1):
            self.ui.b1_3.setText(str(numeroFicha))
            self.ui.b1_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==3 and columna ==2):
            self.ui.b2_3.setText(str(numeroFicha))
            self.ui.b2_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==3 and columna ==3):
            self.ui.b3_3.setText(str(numeroFicha))
            self.ui.b3_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==3 and columna ==4):
            self.ui.b4_3.setText(str(numeroFicha))
            self.ui.b4_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==3 and columna ==5):
            self.ui.b5_3.setText(str(numeroFicha))
            self.ui.b5_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==3 and columna ==6):
            self.ui.b6_3.setText(str(numeroFicha))
            self.ui.b6_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==3 and columna ==7):
            self.ui.b7_3.setText(str(numeroFicha))
            self.ui.b7_3.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        #fila 4
        if(fila==4 and columna ==0):
            self.ui.b0_4.setText(str(numeroFicha))
            self.ui.b0_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==4 and columna ==1):
            self.ui.b1_4.setText(str(numeroFicha))
            self.ui.b1_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==4 and columna ==2):
            self.ui.b2_4.setText(str(numeroFicha))
            self.ui.b2_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==4 and columna ==3):
            self.ui.b3_4.setText(str(numeroFicha))
            self.ui.b3_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==4 and columna ==4):
            self.ui.b4_4.setText(str(numeroFicha))
            self.ui.b4_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==4 and columna ==5):
            self.ui.b5_4.setText(str(numeroFicha))
            self.ui.b5_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==4 and columna ==6):
            self.ui.b6_4.setText(str(numeroFicha))
            self.ui.b6_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==4 and columna ==7):
            self.ui.b7_4.setText(str(numeroFicha))
            self.ui.b7_4.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        #fila 5
        if(fila==5 and columna ==0):
            self.ui.b0_5.setText(str(numeroFicha))
            self.ui.b0_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==5 and columna ==1):
            self.ui.b1_5.setText(str(numeroFicha))
            self.ui.b1_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==5 and columna ==2):
            self.ui.b2_5.setText(str(numeroFicha))
            self.ui.b2_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==5 and columna ==3):
            self.ui.b3_5.setText(str(numeroFicha))
            self.ui.b3_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==5 and columna ==4):
            self.ui.b4_5.setText(str(numeroFicha))
            self.ui.b4_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==5 and columna ==5):
            self.ui.b5_5.setText(str(numeroFicha))
            self.ui.b5_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==5 and columna ==6):
            self.ui.b6_5.setText(str(numeroFicha))
            self.ui.b6_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        if(fila==5 and columna ==7):
            self.ui.b7_5.setText(str(numeroFicha))
            self.ui.b7_5.setIcon(QtGui.QIcon("Img Linja/torre_"+colorFicha+".png"))#con esto se dibuja en la ficha
        
            
        
           

if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    myapp = ejecutarGame()
    myapp.show()
    sys.exit(app.exec_())
   
    