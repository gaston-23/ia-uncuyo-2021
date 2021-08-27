from random import choices,randint

class Agent:
    pos_act = [0,0]
    piso = []
    ERROR_MOV = "Error en el movimiento, excede los limites"
    random_ag = False
    ind_suc_ini = 0
    limpios = 0

    def __init__(self,ini_x,ini_y,tablero,rand = False):
        self.pos_act = [ini_x,ini_y]
        self.piso = tablero
        self.random_ag = rand
        self.ind_suc_ini = self.piso.get_suciedad()[1]
    
    def calcula_eficiencia(self):
        if  self.ind_suc_ini == 0 :
            return 1
        else:
            return 1 - (self.piso.get_suciedad()[1] / self.ind_suc_ini)

    def mueve_arriba(self):
        if self.piso.permite_mover(self.pos_act[0]-1,self.pos_act[1]):
            self.pos_act[0] -= 1
            return 1
        else:
            # print(self.ERROR_MOV)
            return 0
    
    def mueve_abajo(self):
        if self.piso.permite_mover(self.pos_act[0]+1,self.pos_act[1]):
            self.pos_act[0] += 1
            return 1
        else:
            #print(self.ERROR_MOV)
            return 0

    def mueve_izq(self):
        if self.piso.permite_mover(self.pos_act[0],self.pos_act[1]-1):
            self.pos_act[1] -= 1
            return 1
        else:
            #print(self.ERROR_MOV)
            return 0

    def mueve_derecha(self):
        if self.piso.permite_mover(self.pos_act[0],self.pos_act[1]+1):
            self.pos_act[1] += 1
            return 1
        else:
            #print(self.ERROR_MOV)
            return 0

    def limpia(self):
        if(self.piso.get_casilla(self.pos_act[0],self.pos_act[1]) == 'S'):
            self.piso.set_casilla(self.pos_act[0],self.pos_act[1],'L')
            return 2
        # else:
            # print("El piso en esa posicion estaba limpio, se perdio el movimiento")

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
                if res == 2:
                    res -=1
                    self.limpios += 1
                

            steps += res

            if self.piso.get_suciedad()[0] == 0 :
                steps +=  1000
            
