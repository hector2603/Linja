'''
Created on 11/05/2016

@author: Hector Ocampo
'''

class Tablero(object):
    __Tablerito = 0


    def __init__(self):
        __Tablerito = [[2,1,1,1,1,1,1,1],[2,0,0,0,0,0,0,1],[2,0,0,0,0,0,0,1],[2,0,0,0,0,0,0,1],[2,0,0,0,0,0,0,1],[2,2,2,2,2,2,2,1],]
        for row in __Tablerito:
            print row
        print __Tablerito[0][0]