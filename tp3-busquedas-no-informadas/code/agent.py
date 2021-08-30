from node import node
from environment import environment
from prio_queue import prio_queue

class agent:
    pos_act = None
    piso = []
    ERROR_MOV = "Error en el movimiento, excede los limites"
    visitados = list()
    

    def __init__(self,tablero : environment):
       
        self.piso = tablero 
        self.pos_act = tablero.get_pos_ini()
    
    
    def calcula_BFS(self) -> node:
        frontera = prio_queue()
        visitados = list()

        aux_ini = node(self.pos_act,0)
        frontera.insert(aux_ini)

        while not frontera.is_empty()  :
            aux = frontera.pop()
            if self.piso.get_casilla(aux.pos) == 'O' :
                return aux
            for i in range (4) :
                if i%4 == 0 :
                    pos = (aux.pos[0]-1,aux.pos[1])
                elif i%4 == 1  :
                    pos = (aux.pos[0]+1,aux.pos[1])
                elif i%4 == 2 :
                    pos = (aux.pos[0],aux.pos[1]-1)
                else :
                    pos = (aux.pos[0],aux.pos[1]+1)

                if self.piso.get_casilla(pos) != 'X' :
                    aux_h = frontera.exist(pos)

                    if visitados.count(pos) == 0 and aux_h == False :
                        aux_h = node(pos,aux.costo+1)
                        frontera.insert(aux_h)
                        aux_h.set_padre(aux)
                
            visitados.append(aux.pos)
        print("No hay solucion")
        return aux_ini

    def calcula_DFS(self) -> node:
        

        aux_ini = node(self.pos_act,0)
        # frontera.insert(aux_ini)
        sol = self.DFS_rec(aux_ini)
        if sol == None :
            print("No hay solucion")
        return sol

        
    def DFS_rec(self,aux):
        if self.piso.get_casilla(aux.pos) == 'O' :
            return aux
        if aux.costo >= 5* self.piso.len_x :
            return None
        self.visitados.append(aux.pos)
        for i in range (4) :
            if i%4 == 0 :
                pos = (aux.pos[0]+1,aux.pos[1])
            elif i%4 == 1  :
                pos = (aux.pos[0]-1,aux.pos[1])
            elif i%4 == 2 :
                pos = (aux.pos[0],aux.pos[1]+1)
            else :
                pos = (aux.pos[0],aux.pos[1]-1)

            if self.piso.get_casilla(pos) != 'X' and self.visitados.count(pos) == 0 :

                aux_h = node(pos,aux.costo+1)
                aux_h.set_padre(aux)
                sol = self.DFS_rec(aux_h)
                if sol != None:
                    return sol
                
            
        
        return None

    def calcula_unif(self):
        frontera = prio_queue()
        visitados = list()

        aux_ini = node(self.pos_act,0)
        frontera.insert(aux_ini,prio=True)

        while not frontera.is_empty()  :
            aux = frontera.pop()
            if self.piso.get_casilla(aux.pos) == 'O' :
                return aux
            for i in range (4) :
                if i%4 == 0 :
                    pos = (aux.pos[0]-1,aux.pos[1])
                elif i%4 == 1  :
                    pos = (aux.pos[0]+1,aux.pos[1])
                elif i%4 == 2 :
                    pos = (aux.pos[0],aux.pos[1]-1)
                else :
                    pos = (aux.pos[0],aux.pos[1]+1)

                if self.piso.get_casilla(pos) != 'X' :
                    aux_h = frontera.exist(pos)

                    if visitados.count(pos) == 0 :
                        if aux_h == False :
                            aux_h = node(pos,aux.costo+1)
                            frontera.insert(aux_h,prio=True)
                        elif aux_h.padre != None and aux_h.padre.costo > aux.costo + 1 :
                            frontera.update_idx(aux_h.pos)

                        if aux_h.padre == None or (aux_h.padre != None and aux_h.padre.costo > aux.costo + 1) :
                            aux_h.set_padre(aux)
                
            visitados.append(aux.pos)
        print("No hay solucion")
        return aux_ini

