


class prio_queue :
    
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    def is_empty(self):
        return len(self.queue) == 0
  
    def insert(self, data,key):
        aux = Nodo(data,key)
        for i in range(len(self.queue)):
            if self.queue[i].key > key:
                
                self.queue.insert(i, aux)
                return
        self.queue.append(aux)
  
    def pop(self):
        if len(self.queue) == 0 :
            return None
        else:
            return self.queue.pop(len(self.queue)-1)
    
    def exist(self,data_n):
        for i in self.queue:
            if i.data == data_n :
                return i
        return False
    
    
    def get(self,idx):
        return self.queue[idx];

    def __len__(self):
        return len(self.queue)

    

class Nodo:

    def __init__ (self,data,key):
        self.data = data
        self.key = key

    def __str__ (self):
        return self.key