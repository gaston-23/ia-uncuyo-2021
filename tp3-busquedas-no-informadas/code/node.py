





class node:
    pos = None
    padre = None
    hijo = None
    costo = 0

    def __init__(self,pos: tuple, cost: int):
        self.pos = pos
        self.hijo = list()
        self.costo = cost
        
    def __str__ (self):
        return str(self.pos)
        
    def camino(self):
        if self.padre == None :
            return  str(self.pos)
        else :
            return self.padre.camino() + '->' + str(self.pos)

    def set_padre(self,parent):
        self.padre = parent

    def set_costo(self, cost):
        self.costo = cost
    
    def add_hijo(self, child):
        self.hijo.append(child)

    