
from random import choices,randint


class environment:

    tablero = []
    suc_ini = 0
    len_x = 10
    len_y = 10
    part_x = 0
    part_y = 0

    def __init__(self,partida_aleatoria = True,testing = ""):  
        if testing == "" :      
            pop = [' ','X']
            ran_x = randint(0,self.len_x-1)
            ran_y = randint(0,self.len_y-1)
            if partida_aleatoria :
                self.part_x = randint(0,self.len_x-1)
                self.part_y = randint(0,self.len_y-1)
            for i in range (self.len_x)  :
                assign = choices(pop, weights=[0.8,0.4], k=self.len_y)
                if i == self.part_x :
                    assign[self.part_y] = 'S'
                if i == ran_x :
                    assign[ran_y] = 'O'
                self.tablero.append(assign)
        else:
            for i in testing.split("\n"):
                assign = list()
                for j in i.split("| "):
                    aux = j.strip(" |")
                    if aux == "":
                        aux = ' '
                    assign.append(aux)
                    if aux == 'S':
                        self.part_x = len(self.tablero)
                        self.part_y = len(assign)-1
                self.tablero.append(assign)



    
    def __str__(self) -> str:
        res = ''
        for i in range(len(self.tablero)):
            res += '|'
            for j in range(len(self.tablero[i])):
                if self.tablero[i][j] == 'S':
                    res += ' \033[91m\033[1m'+self.tablero[i][j]+' \033[0m|'
                elif self.tablero[i][j] == 'O':
                    res += ' \033[96m\033[1m'+self.tablero[i][j]+' \033[0m|'
                else:
                    res+=' '+self.tablero[i][j]+' |'

            res += '\n'
        return res

    def print_pos(self,pos):
        res = ''
        for i in range(len(self.tablero)):
            res += '|'
            for j in range(len(self.tablero[i])):
                if self.tablero[i][j] == 'S':
                    res += ' \033[91m\033[1m'+self.tablero[i][j]+' \033[0m|'
                elif self.tablero[i][j] == 'O':
                    res += ' \033[96m\033[1m'+self.tablero[i][j]+' \033[0m|'
                elif i == pos[0] and j == pos[1]:
                    res+=' A |'
                else:
                    res+=' '+self.tablero[i][j]+' |'

            res += '\n'
        return res
    
    def get_casilla(self,pos) -> str:
        if pos[0] < self.len_x and pos[1] < self.len_y and pos[0] >= 0 and pos[1] >= 0 :
            return self.tablero [pos[0]] [pos[1]]
        else:
            return 'X'
    
    def get_pos_ini (self) -> tuple:
        return (self.part_x,self.part_y)
    
        