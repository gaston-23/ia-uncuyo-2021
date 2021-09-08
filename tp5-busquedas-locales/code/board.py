from random import randint
from typing import Sized
from queen import queen



class board:

    def __init__(self,queens) -> None:
        '''
        queens {int} : define la cantidad de reinas y por ende el largo y ancho del tablero
        '''
        self.tablero = list()
        self.queens = list()
        for i in range(queens):
            assign = list()
            aux = randint(0,queens-1)
            for j in range(queens):
                if j == aux:
                    q = queen(i,j)
                    assign.append(q)
                    self.queens.append(q)
                    # assign.append('Q')
                else:
                    assign.append(' ')
            self.tablero.append(assign)
        

    def calcula_match(self,pos_i,pos_j):
        match = 0
        for i in range(len(self.tablero)):
            # for j in range(len(self.tablero)):

            #     if j == pos_j and self.tablero[i][j] == 'Q' and i != pos_i:
            #         match += 1
            #     if abs(pos_j - j) == abs(pos_i - i) and self.tablero[i][j] == 'Q' and i != pos_i:
            #         match += 1 
            if i != pos_i:
                for j in range(len(self.tablero)):
                    if j == pos_j and isinstance(self.tablero[i][j], queen) :
                        match += 1
                    if abs(pos_j - j) == abs(pos_i - i) and isinstance(self.tablero[i][j], queen) :
                        match += 1 
        if isinstance(self.tablero[pos_i][pos_j], queen):
            self.tablero[pos_i][pos_j].valor = match
        return match

    def __str__(self) -> str:
        res = ''
        for i in range(len(self.tablero)):
            res += '|'
            for j in range(len(self.tablero[i])):
                res+=' '+str(self.tablero[i][j])+' |'

            res += '\n'
        return res

    def get_mapa(self,skip:list):
        res = list()
        minis = list()
        for i in range(len(self.tablero)):
            aux = list()
            min_loc = 0
            for j in range(len(self.tablero[i])):
                casilla = self.calcula_match(i,j)
                aux.append(casilla)
                
                #print(res,minis,len(res),sep='->')
                if casilla < aux[min_loc]:
                    min_loc = j
            res.append(aux)
            if skip.count(i) == 0:
                minis.append((i,min_loc))
        # print(res)
        top = [0,0,0]
        
        for i in self.queens:
            print(i,i.valor, sep='->')
            if i.valor < 3 :
                top[i.valor] += 1
        # print(top)
        mini = 99
        print(minis)
        final_res = list()
        for i in minis :
            if res[i[0]][i[1]] < mini :
                final_res.clear()
                mini = res[i[0]][i[1]]
                
            if res[i[0]][i[1]] == mini :
                final_res.append(i)
                
        best = final_res[randint(0,len(final_res)-1)]
        # print(best)
        # for i in range(len(self.tablero)) :
        #     if self.tablero[best[0]][i] == 'Q':
        #         self.tablero[best[0]][i] = ' '
        print(best[0],self.queens[best[0]].j,best[1])
        self.move_queen(best[0],self.queens[best[0]].j,best[1])

        return (3*top[0] + 2*top[1] + 1*top[2], best[0])
    
    def move_queen(self,i,old_j,new_j):
        act_q = self.queens[i]
        self.tablero[i][old_j] = ' '
        self.tablero[i][new_j] = act_q
        act_q.j = new_j
    

    def hill_climb(self,resto):
        max_i = 0
        k = 0
        skip = list()
        while k < 1000 and max_i < len(self.tablero)*3-resto :
            (max_i,aux_skip) = self.get_mapa(skip)
            skip.append(aux_skip)
            if len(skip) > len(self.tablero)*0.8:
                skip.clear()
            print('it -> ',k,' | valor: ',max_i)

            print(self)
            k += 1