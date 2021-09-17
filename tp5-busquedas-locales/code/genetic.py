from hashlib import new
from random import randint, random
from board import board
from prio_queue import prio_queue

class genetic:

    pob_ini = 200


    def __init__(self,queens):
        self.poblacion = prio_queue()
        for i in range(self.pob_ini):
            aux = board(queens)
            self.queens = queens
            # aux.get_mapa()
            punt = aux.get_punt_sa(aux.queens)
            self.poblacion.insert(data=aux,key=punt)

    def encuentra_exito(self):
        if self.poblacion.get(0).key == 0 :
            return self.poblacion.get(0).data
        return 0

    
    def seleccion(self):
        aux = prio_queue()
        for i in range(int(self.pob_ini*0.1)):
            aux.insert(self.poblacion.get(i).data,self.poblacion.get(i).key)
        return aux

    def crossover(self,pob):
        '''
        agrega la cantidad de filas de un tablero, de acuerdo a un numero aleatorio
        '''
        new_pob = prio_queue()
        tot_fit = 0
        for i in range(len(pob)):
            tot_fit += pob.get(i).key
        i = 0
        while(len(new_pob)<len(pob)):
            i = randint(0,len(pob)-1)
            j = randint(0,len(pob)-1)
            prob = random()
            x = pob.get(i).data
            y = pob.get(j).data

            while ( prob <(self.queens**2 - pob.get(i).key )/tot_fit and prob <(self.queens**2 - pob.get(j).key )/tot_fit ):
                i = randint(0,len(pob)-1)
                j = randint(0,len(pob)-1)
                prob = random()
            

            filas = randint(0,self.queens)

            aux_1 = self.cruza(x,y,filas)
            aux_2 = self.cruza(y,x,filas)
            punt_1 = aux_1.get_punt_sa(aux_1.queens)
            new_pob.insert(aux_1,punt_1)
            
            punt_2 = aux_2.get_punt_sa(aux_2.queens)
            new_pob.insert(aux_2,punt_2)
        # self.calcular_fit(new_pob)
        for i in range(len(pob)//5):
            new_pob.insert(pob.get(i).data,pob.get(i).key)
            new_pob.pop()
        self.calcular_fit(new_pob)
        # for i in range(len(pob)):
            
        #     new_pob.insert(x,pob.get(i).key)
        #     for j in range(i+1,len(pob)):
                
        #         filas = randint(0,self.queens)
        #         y = pob.get(j).data
                
        #         aux_1 = self.cruza(x,y,filas)
        #         aux_2 = self.cruza(y,x,filas)
        #         punt_1 = aux_1.get_punt_sa(aux_1.queens)
        #         new_pob.insert(aux_1,punt_1)
                
        #         punt_2 = aux_2.get_punt_sa(aux_2.queens)
        #         new_pob.insert(aux_2,punt_2)

        return new_pob

    def cruza(self,padre,madre,filas):
        hijo = board(self.queens,auto=False)
        hijo.agrega_fil(padre.extraer_filas(filas,True))
        hijo.agrega_fil(madre.extraer_filas(self.queens-filas-1,False))
        hijo.get_mapa()
        
        return hijo
                
    def mutacion(self,pob):
        
        for i in range(len(pob)):
            muta = random()
            if muta <= 0.1:
                pob.get(i).data.mutar()
        return pob

    def calcular_fit(self,pob):
        aux = prio_queue()
        for i in range(len(pob)):
            actual = pob.get(i).data
            # actual.get_mapa()
            punt = actual.get_punt_sa(actual.queens)
            aux.insert(actual,punt)
        res = 0
        for i in range(len(aux)):
            res += aux.get(i).key
        return (res / self.pob_ini),aux


    def seleccion_ga(self):
        k=0

        while self.encuentra_exito() == 0 and k<1000 :
            k+=1
            # next_pob = self.seleccion()
            next_pob = self.crossover(self.poblacion)
            next_pob = self.mutacion(next_pob)
            fit_old,self.poblacion =  self.calcular_fit(self.poblacion)
            fit_new,next_pob = self.calcular_fit(next_pob)
            delta = fit_old - fit_new
            print("delta:: ",delta,"fit a: ",fit_old,"fit b: ",fit_new)
            # if delta > 0 :
            self.poblacion = next_pob 
            print("k ->",k, " max 0: ",self.poblacion.get(0).key, " // ", len(self.poblacion))
            # print(self.poblacion.get(0).data)
            print("========================================================")
            # else:
            #     next_pob,idx = self.mutacion(next_pob)
            #     print(next_pob.get(idx).data)
            #     fit_new,next_pob = self.calcular_fit(next_pob)
            #     delta = fit_old - fit_new
            #     print("new_delta::  ",delta,"fit a: ",fit_old,"fit b: ",fit_new)
            #     self.poblacion = next_pob 
            #     # for i in range(len(self.poblacion)):
            #     #     print(self.poblacion.get(i).data)
            # print("k ->",k, " max 0: ",self.poblacion.get(0).key, " // ", len(self.poblacion))
        print(self.poblacion.get(0).data)
        print(self.poblacion.get(0).key)
        print(self.poblacion.get(0).data.get_punt_sa(self.poblacion.get(0).data.queens))
        # print(self.poblacion.get(0).data)
        return self.poblacion.get(0).data,self.poblacion.get(0).key,k