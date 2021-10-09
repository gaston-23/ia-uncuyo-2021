
from time import time;
from random import randint

class queen_back:

    def __init__(self,cant,back = True ):
        self.AMM_QUEENS = cant
        self.queens = list()
        i=0
        recorridos = 0
        start = time()
        if back:
            while (len(self.queens) < self.AMM_QUEENS):
                if(i >= self.AMM_QUEENS):
                    if len(self.queens) == 0:
                        print("Error de implementacion")
                    i = self.queens.pop() +1
                else:
                    self.queens.append(i)
                    recorridos += 1
                    if(not self.is_solution()):
                        i+=1
                        self.queens.pop()
                    else:
                        i = 0
        else:
            while (len(self.queens) < self.AMM_QUEENS):
                if(i >= self.AMM_QUEENS):
                    if len(self.queens) == 0:
                        print("Error de implementacion")
                    i = self.queens.pop() +1
                else:
                    if not self.is_ban(len(self.queens),i):
                        self.queens.append(i)
                        recorridos += 1
                        if(not self.is_solution()):
                            i+=1
                            self.queens.pop()
                        else:
                            i = 0
                    else :
                        i+=1
        end = time()
        if back :
            metodo = "backtracking"
        else:
            metodo = "forward checking"
        print("Para "+str(self.AMM_QUEENS)+" reinas, utilizando "+metodo)
        print("tiempo: ",end - start)
        print("estados recorridos: ",recorridos)
                    
    def is_ban(self,i,j):
        for k in self.queens:
            if self.queens.index(k) != i and k==j:
                return True
            if abs(self.queens.index(k) - i) == abs(k - j) and self.queens.index(k) != i :
                return True
        return False


        
    def is_solution(self):
        for i in range(len(self.queens)) :
            for j in range(len(self.queens)) :
                if self.queens[i] == self.queens[j] and i!=j :
                    return False
                if abs(i - j) == abs(self.queens[i] - self.queens[j]) and i!=j :
                    return False
        return True

    def __str__(self) -> str:
        res = ''
        for i in range(self.AMM_QUEENS-1):
            res += '|'
            for j in range(self.AMM_QUEENS-1):
                if i< len(self.queens) and self.queens[i] == j :
                    res+=' Q |'
                else:
                    res+='   |'

            res += '\n'
        return res
