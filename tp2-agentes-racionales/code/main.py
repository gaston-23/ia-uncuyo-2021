

from random import choices,randint


class Environment:
    tablero = []
    def __init__(self,len_x,len_y,dirt_p):
        pop = ['L','S']
        for i in range (len_x)  :
            self.tablero.append(choices(pop, weights=[1-dirt_p,dirt_p],k=len_y))
    
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

    def get_porcentaje_suciedad(self):
        res = 0.0
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if(self.tablero[i][j] == 'S'):
                    res += 1
        tot = len(self.tablero[0])*len(self.tablero)
        return (res / tot)
    
    def permite_mover(self,pos_x,pos_y):
        if pos_x < len(self.tablero) and pos_x >= 0 and pos_y < len(self.tablero[0]) and pos_y >= 0:
            return True
        else:
            return False
        
class Agent:
    pos_act = [0,0]
    piso = []
    ERROR_MOV = "Error en el movimiento, excede los limites"
    random_ag = False
    ind_suc_ini = 0

    def __init__(self,ini_x,ini_y,tablero,rand = False):
        self.pos_act = [ini_x,ini_y]
        self.piso = tablero
        self.random_ag = rand
        self.ind_suc_ini = self.piso.get_porcentaje_suciedad()
    
    def calcula_eficiencia(self):
        return 1 - (self.piso.get_porcentaje_suciedad() / self.ind_suc_ini)

    def mueve_arriba(self):
        if self.piso.permite_mover(self.pos_act[0]-1,self.pos_act[1]):
            self.pos_act[0] -= 1
            return 1
        else:
            print(self.ERROR_MOV)
            return 0
    
    def mueve_abajo(self):
        if self.piso.permite_mover(self.pos_act[0]+1,self.pos_act[1]):
            self.pos_act[0] += 1
            return 1
        else:
            print(self.ERROR_MOV)
            return 0

    def mueve_izq(self):
        if self.piso.permite_mover(self.pos_act[0],self.pos_act[1]-1):
            self.pos_act[1] -= 1
            return 1
        else:
            print(self.ERROR_MOV)
            return 0

    def mueve_derecha(self):
        if self.piso.permite_mover(self.pos_act[0],self.pos_act[1]+1):
            self.pos_act[1] += 1
            return 1
        else:
            print(self.ERROR_MOV)
            return 0

    def limpia(self):
        if(self.piso.get_casilla(self.pos_act[0],self.pos_act[1]) == 'S'):
            self.piso.set_casilla(self.pos_act[0],self.pos_act[1],'L')
        else:
            print("El piso en esa posicion estaba limpio, se perdio el movimiento")
        return 1

    def idle(self):
        return 1
    
    def calcula(self):
        steps = 0
        #si es random
        while(steps<1000):
            if(self.random_ag):
                opc = randint(0, 5)
            else:
                if(self.piso.get_casilla(self.pos_act[0],self.pos_act[1]) == 'S'):
                    opc = 5
                else:
                    opc = randint(1, 4)

            if opc == 0:
                res = self.idle()
            elif opc == 1:
                res = self.mueve_izq()
            elif opc == 2:
                res = self.mueve_abajo()
            elif opc == 3:
                res = self.mueve_arriba()
            elif opc == 4:
                res = self.mueve_derecha()
            else:
                res = self.limpia()

            steps += res


    
    

        



p = Environment(100,10,0.9)
a = Agent(3,0,p)
# print(p.get_porcentaje_suciedad())
a.calcula()
print(a.ind_suc_ini)
print(p.get_porcentaje_suciedad())
print(a.calcula_eficiencia())

    
