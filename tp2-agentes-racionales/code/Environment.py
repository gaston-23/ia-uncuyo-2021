
from random import choices,randint


class Environment:
    tablero = []
    suc_ini = 0
    def __init__(self,len_x,len_y,dirt_p):
        left = int(len_x * len_y * dirt_p)
        if dirt_p != 0 and left == 0 :
            left = 1
        
        
        pop = ['L','S']
        for i in range (len_x)  :
            if left > 0 :
                assign = choices(pop, weights=[1-dirt_p,dirt_p],k=len_y)
            else :
                assign = choices(pop, weights=[1,0],k=len_y)
            self.tablero.append(assign)
            left -= assign.count('S')

        for i in range(left) :
            ind_i = randint(0,len_x-1)
            ind_j = randint(0,len_y-1)
            if self.tablero[ind_i][ind_j] == 'L':
                self.tablero[ind_i][ind_j] = 'S'
        self.suc_ini = self.get_suciedad()[0]


    
    def __str__(self):
        res = ''
        for i in range(len(self.tablero)):
            res += '|'
            for j in range(len(self.tablero[i])):
                res+='  '+self.tablero[i][j]+'  |'
            res += '\n'
        return res
    
    def get_casilla(self,x,y):
        return self.tablero[x][y]
    
    def set_casilla(self,x,y,value):
        self.tablero[x][y] = value
        return 1


    def get_suciedad(self):
        ''' Devuelve un array dado por [cant de suciedad, porcentaje de suciedad]
        '''
        res = 0.0
        for i in range(len(self.tablero)):
            res += self.tablero[i].count('S')
        tot = len(self.tablero[0])*len(self.tablero)
        return res,(res / tot)
    
    def permite_mover(self,pos_x,pos_y):
        if pos_x < len(self.tablero) and pos_x >= 0 and pos_y < len(self.tablero[0]) and pos_y >= 0:
            return True
        else:
            return False
        