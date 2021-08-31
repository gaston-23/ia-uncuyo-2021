from node import node
from environment import environment
from prio_queue import prio_queue

class agent:
    
    
    def __init__(self,tablero : environment):
       
        self.piso = tablero 
        self.pos_act = tablero.get_pos_ini()
        self.eficiencia = 0
    
    
    def calcula_star(self):
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
                            heur = self.piso.get_dist(pos)
                            aux_h = node(pos,aux.costo+1 + heur)
                            self.eficiencia += 1
                            frontera.insert(aux_h,prio=True)
                            aux_h.set_padre(aux)
                        elif aux_h.padre != None and aux_h.padre.costo > (aux.costo + 1) :
                            frontera.update_idx(aux_h.pos)
                            aux_h.set_padre(aux)                            
                
            visitados.append(aux.pos)
        print("No hay solucion")
        return aux_ini
    
    

