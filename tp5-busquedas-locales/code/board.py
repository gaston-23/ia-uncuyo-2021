from random import randint, random
from typing import Sized
from queen import queen
from math import exp


class board:

    def __init__(self,queens,auto=True) -> None:
        '''
        queens {int} : define la cantidad de reinas y por ende el largo y ancho del tablero
        '''
        self.tablero = list()
        self.queens = list()
        if auto:
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

    def agrega_fil(self,filas):
        for i in filas:
            for j in range(len(i)):
                if isinstance(i[j],queen):
                    i[j].i = filas.index(i)
                    i[j].j = j
                    self.queens.append(i[j])
            self.tablero.append(i)


    def calcula_match(self,pos_i,pos_j):
        '''
        calcula la puntuacion de la casilla
        '''
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

    def get_mapa(self):
        res = list()
        minis = list()
        for i in range(len(self.tablero)):
            aux = list()
            min_loc = 0
            for j in range(len(self.tablero[i])):
                casilla = self.calcula_match(i,j)
                aux.append(casilla)
                if aux[min_loc] > casilla :
                    min_loc = j
            for j in range(len(self.tablero[i])):
                if aux[j] <= aux[min_loc] :
                    minis.append((i,j))
            res.append(aux)
        return res,minis

    def seleccion_hc(self,skip:list):
        '''
        obtiene las puntuaciones del mapa y una lista de posibles movimientos, si la fila que revisa esta en skip, no añade esa fila a los posibles movimientos
        al finalizar, elije uno de los mejores escenarios aleatoriamente y retorna la puntuacion del tablero junto con la reina elegida
        '''
        res,minis_aux = self.get_mapa()

        minis = list()
        for i in minis_aux:
            if skip.count(i[0]) == 0:
                minis.append(i)
        
        mini = 99
        # print(minis)
        final_res = list()
        for i in minis :
            if res[i[0]][i[1]] < mini :
                final_res.clear()
                mini = res[i[0]][i[1]]
                
            if res[i[0]][i[1]] == mini :
                final_res.append(i)
                
        best = final_res[randint(0,len(final_res)-1)]
        # print(best)
        # print(best[0],self.queens[best[0]].j,best[1])
        self.move_queen(best[0],best[1],res[best[0]][best[1]])

        return (self.get_valorizacion(), best[0])

    def get_valorizacion(self):
        top = [0,0,0]
        for i in self.queens:
            # print(i,i.valor, sep='->')
            if i.valor < 3 :
                top[i.valor] += 1
        return 3*top[0] + 2*top[1] + 1*top[2]
    
    def move_queen(self,i,new_j,valor):
        '''
        mueve la reina en la fila i de la posicion old_j a new_j
        '''
        act_q = self.queens[i]
        self.tablero[i][act_q.j] = ' '
        self.tablero[i][new_j] = act_q
        act_q.j = new_j
        act_q.valor = valor
    
    def hill_climb(self,resto):
        '''
        algoritmo para hill climbing, donde el resto es el margen de error que le queremos dar (cuantos 1 estan permitidos en la solucion)

        '''
        max_i = 0
        k = 0
        skip = list()
        while k < 1000 and max_i < len(self.tablero)*3-resto :
            (max_i,aux_skip) = self.seleccion_hc(skip) #obtiene la puntuacion del mapa y la reina que cambio de posicion
            skip.append(aux_skip) #añade la reina a la lista de excepciones para evitar entrar en un optimo local
            if len(skip) > len(self.tablero)*0.8: #cuando la lista es suficientemente grande, se limpia
                skip.clear()
            # print('it -> ',k,' | valor: ',max_i)

            # print(self)
            k += 1
        return k

    def get_punt_sa(self,queens):
        self.get_mapa()
        sum_tot = 0
        for i in queens:
            sum_tot += i.valor
        return sum_tot

    def seleccion_sa(self,t,old):
        temp = self.temp_sched(t)
        # print("temp:",temp)

        res,minis_aux = self.get_mapa()
        if temp == 0:
            return old
        minis = list()
        # minis = minis_aux
        # print("res::\n",self.print_res(res))
        # for i in minis_aux:
        #     print(i,'->',self.queens[i[0]].i,self.queens[i[0]].j)
        #     if i[1] != self.queens[i[0]].j :
        #         minis.append(i)
        mini = 99
        for i in minis_aux :
            if self.queens[i[0]].valor > 0  and self.queens[i[0]].j != i[1] :
                if res[i[0]][i[1]] < mini:
                    minis.clear()
                    mini = res[i[0]][i[1]]
                    
                if res[i[0]][i[1]] == mini :
                    minis.append(i)
        # for i in minis:
            # print(i,res[i[0]][i[1]])
        if len(minis) == 0:
            return self.get_punt_sa(self.queens)
        rand_best = minis[randint(0,len(minis)-1)]
        # print(rand_best)
        new_queens = self.queens
        new_queens[rand_best[0]].valor = res[rand_best[0]][rand_best[1]]
        delta_e = self.get_punt_sa(new_queens) - old 
        if delta_e < 0 or random() <= self.prob(temp,delta_e):
            # print("d: ",delta_e,"::",self.prob(temp,delta_e))
            self.move_queen(rand_best[0],rand_best[1],res[rand_best[0]][rand_best[1]])
        return self.get_punt_sa(self.queens)

    def temp_sched(self,t):
        return 1/t

    def prob(self,temp,delta):
        return exp(delta/temp)

    def sim_ann(self,resto):
        '''
        algoritmo para simulated annealing, donde el resto es el margen de error que le queremos dar (cuantos 1 estan permitidos en la solucion)
        '''
        max_i = 100
        k = 1
        # skip = list()
        while k < 1000 and max_i > resto :
            max_i = self.seleccion_sa(k,max_i)
            # skip.append(aux_skip)
            # if len(skip) > len(self.tablero)*0.8:
            #     skip.clear()
            # print('it -> ',k,' | valor: ',max_i)

            # print(self)
            k += 1
        return k

    def print_res(self,res):
        resl = ''
        for i in range(len(res)):
            resl += '|'
            for j in range(len(res[i])):
                resl+=' '+str(res[i][j])+' |'

            resl += '\n'
        return resl

    def extraer_filas(self,cant,inicio):
        aux = list()
        if inicio:
            for i in range(cant):
                aux.append(self.tablero[i])
        else:
            for i in range(len(self.tablero)-cant-1, len(self.tablero)):
                aux.append(self.tablero[i])
        return aux
    
    def mutar(self):
        ran_x = randint(0,len(self.tablero)-1)
        ran_y = randint(0,len(self.tablero)-1)
        res,minis_aux = self.get_mapa()
        self.move_queen(ran_x,ran_y,res[ran_x][ran_y])

    