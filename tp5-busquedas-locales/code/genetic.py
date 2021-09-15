from random import randint
from board import board
from prio_queue import prio_queue

class genetic:

    pob_ini = 100


    def __init__(self,queens):
        self.poblacion = prio_queue()
        for i in range(self.pob_ini):
            aux = board(queens)
            self.queens = queens
            aux.get_mapa()
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
        for i in range(len(pob)):
            x= pob.get(i).data
            new_pob.insert(x,pob.get(i).key)
            for j in range(i+1,len(pob)):
                
                filas = randint(0,self.queens)
                y = pob.get(j).data
                
                aux_1 = self.cruza(x,y,filas)
                aux_2 = self.cruza(y,x,filas)
                punt_1 = aux_1.get_punt_sa(aux_1.queens)
                new_pob.insert(aux_1,punt_1)
                
                punt_2 = aux_2.get_punt_sa(aux_2.queens)
                new_pob.insert(aux_2,punt_2)

        return new_pob

    def cruza(self,padre,madre,filas):
        hijo = board(self.queens,auto=False)
        hijo.agrega_fil(padre.extraer_filas(filas,True))
        hijo.agrega_fil(madre.extraer_filas(self.queens-filas-1,False))
        hijo.get_mapa()
        
        return hijo




                
    def mutacion(self,pob):
        printed = True
        idx = 0
        for i in range(len(pob)):
            muta = randint(0,1)
            if muta:
                if printed:
                    print("GEN:: ",muta)
                    print(pob.get(i).data)
                pob.get(i).data.mutar()
                if printed:
                    print(pob.get(i).data)
                    idx = i
                    printed = False


        return pob,idx

    def calcular_fit(self,pob):
        aux = prio_queue()
        for i in range(len(pob)):
            actual = pob.get(i).data
            actual.get_mapa()
            punt = actual.get_punt_sa(actual.queens)
            aux.insert(actual,punt)
        res = 0
        for i in range(len(aux)):
            res += aux.get(i).key
        return (res / self.pob_ini),aux


    def seleccion_ga(self):
        k=0

        while self.encuentra_exito() == 0 and k<100 :
            k+=1
            next_pob = self.seleccion()
            next_pob = self.crossover(next_pob)
            fit_old,self.poblacion =  self.calcular_fit(self.poblacion)
            fit_new,next_pob = self.calcular_fit(next_pob)
            delta = fit_old - fit_new
            print("delta:: ",delta,"fit a: ",fit_old,"fit b: ",fit_new)
            if delta > 0 :
                self.poblacion = next_pob 
                print("k ->",k, " max 0: ",self.poblacion.get(0).key, " // ", len(self.poblacion))
                print(self.poblacion.get(0).data)
                print("========================================================")
            else:
                next_pob,idx = self.mutacion(next_pob)
                print(next_pob.get(idx).data)
                fit_new,next_pob = self.calcular_fit(next_pob)
                delta = fit_old - fit_new
                print("new_delta::  ",delta,"fit a: ",fit_old,"fit b: ",fit_new)
                self.poblacion = next_pob 
                # for i in range(len(self.poblacion)):
                #     print(self.poblacion.get(i).data)
            print("k ->",k, " max 0: ",self.poblacion.get(0).key, " // ", len(self.poblacion))
        print(self.poblacion.get(0).data)
        print(self.poblacion.get(0).key)
        print(self.poblacion.get(0).data.get_punt_sa(self.poblacion.get(0).data.queens))
        # print(self.poblacion.get(0).data)
        return 1