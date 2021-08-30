


class prio_queue:
    queue = []

    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    def is_empty(self):
        return len(self.queue) == 0
  
    def insert(self, data, prio = False):
        if prio:
            prev = 0
            for i in range(len(self.queue)):
                if self.queue[i].cost > self.queue[prev].cost:
                        prev = i
                else:
                    self.queue.insert(prev+1,data)
        else:
            self.queue.append(data)
  
    def pop(self):
        if self.is_empty() :
            return None
        else:
            return self.queue.pop(0)
    
    def exist(self,data):
        for i in self.queue:
            if i.pos == data :
                return i
        return False
    
    def update_idx(self,data):
        for i in self.queue:
            if i.pos == data :
                aux = self.queue.pop(i)
                self.insert(aux,prio=True)
                return i
        return False
