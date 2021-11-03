import math
from os import name


class decision_node:

    def __init__(self,outlook,temp,humidity,windy,play):
        self.outlook = outlook
        self.temp = temp
        self.humidity = humidity
        self.windy = windy
        self.play = play

    def __init__(self,row):
        self.at = dict()
        self.at['outlook'] = row[0]
        self.at['temp'] = row[1]
        self.at['humidity'] = row[2]
        self.at['windy'] = row[3]

        if row[4] == 'yes': self.at['play'] = True
        else: self.at['play'] = False

    def __str__(self) -> str:
        res = ''
        for i in self.at.items():
            res+= str(i)
        # res = 'outlook: '+self.outlook
        # res += ', temp: '+ self.temp 
        # res += ', humidity: '+ self.humidity 
        # res += ', windy: '+ self.windy 
        # res += ', play: '+ self.play +'\n'
        return res
    
    def fit(self,attr:dict):
        for i in attr.items():
            if self.at[i[0]] != i[1]:
                return False
        return True

class decision_attrib:

    def __init__(self,name):
        self.name = name
        self.p = 0
        self.n = 0
        self.entropy = 0
        self.count = 0
        self.resto = 0
        self.gain = 0
        self.ret = False

    def add(self,p):
        self.count += 1
        if p : self.p += 1
        else : self.n += 1

    def __str__(self) -> str:
        res = self.name
        res += '\n\t\t\t p: '+ str(self.p)
        res += '\n\t\t\t n: '+ str(self.n)
        res += '\n\t\t\t entropy: '+ str(self.entropy)
        res += '\n\t\t\t count: ' + str(self.count)
        res += '\n\t\t\t resto: ' + str(self.resto)
        res += '\n\t\t\t gain: ' + str(self.gain)
        if self.ret == True or self.ret == False: res += '\n\t\t\t ret: ' + str(self.ret)
        else: res += '\n\t\t\t ret: ' + str(self.ret.name)
        return res
    
    def calc_entropy(self):
        ep = 0
        en = 0
        if self.count > 0:
            ep = self.p / self.count
            en = self.n / self.count
        if ep == 0:
            if en == 0:
                self.entropy = 0
            else:
                self.entropy = -en * math.log2(en)
        else:
            if en == 0:
                self.entropy = -ep * math.log2(ep)
            else:
                self.entropy = -ep * math.log2(ep) - en * math.log2(en)
    
    def calc_resto(self,total):
        res = self.count / total
        self.resto = res * self.entropy
    
    def calc_gain(self, tot_ent):
        self.gain = tot_ent - self.resto
    
    
class decision_head:

    def __init__(self,name):
        self.name = name
        self.atribs = dict()
        self.used = False
        

    def add_atrib (self, atrib, succ):
        if self.atribs.get(atrib) != None:
            self.atribs.get(atrib).add(succ)
        # if self.exists(atrib): 
            # self.atribs.get_at(atrib).add(succ)
        else:
            aux = decision_attrib(atrib)
            aux.add(succ)
            self.atribs[atrib] = aux
            # self.atribs.append(aux)
        
    def clear(self):
        # if not self.used:
        for i in self.atribs.values():
        
            i.p = 0
            i.n = 0
            i.entropy = 0
            i.count = 0
            i.resto = 0
            i.gain = 0

    def exists(self, atrib) -> bool:
        if self.atribs.get(atrib) == None: return False
        return True
        # for i in self.atribs:
            # if i.name == atrib:
                # return True
        # return False
    
    def get_at(self,atrib) -> decision_attrib:
        for i in self.atribs:
            if i.name == atrib:
                return i
        return None

    def at2str(self) -> str:
        res = ''
        for i in self.atribs.values():
            res += '\t\t'+str(i)+'\n'
        return res
    
    def __str__(self) -> str:
        res = self.name
        
        res += '\n '+ self.at2str()

        return res
    
    def calc_entropy(self, total, entropy ):
        
        for i in self.atribs.values():
            i.calc_entropy()
            i.calc_resto(total)
            i.calc_gain(entropy)



class decision_tree:

    def __init__(self,nodes,head) -> None:
        
        self.head = {
            'outlook':decision_head('outlook'),
            'temp' : decision_head('temp'),
            'humidity' : decision_head('humidity'),
            'windy' : decision_head('windy'),
            }
        self.total_p = 0
        self.total_n = 0
        self.entropy = 0
        self.nodes = nodes
        self.root = None
        self.check = list()

        # for h in range(len(head)-1):
        #     aux_head = decision_head(head[h])
        #     self.head.append(aux_head)
        self.complete(nodes)
        self.treeify()
    
    def complete(self,nodes):
        self.head['outlook'].clear()
        self.head['temp'].clear()
        self.head['humidity'].clear()
        self.head['windy'].clear()
        self.total_p = 0
        self.total_n = 0
        self.entropy = 0
        for i in nodes:
            self.head['outlook'].add_atrib(i.at['outlook'], i.at['play'])
            self.head['temp'].add_atrib(i.at['temp'], i.at['play'])
            self.head['humidity'].add_atrib(i.at['humidity'], i.at['play'])
            self.head['windy'].add_atrib(i.at['windy'], i.at['play'])
            if i.at['play'] : self.total_p += 1
            else : self.total_n += 1
        self.calc_entropy()
        
                
    def __str__(self) -> str:
        res = ''
        res += '\n total_p:'+ str(self.total_p)
        res += '\n total_n:'+ str(self.total_n)
        res += '\n ent:'+ str(self.entropy)+'\n'
        for i in self.head.values():
            res+= '\t'+str(i) + '\n'

        return res
        
    
    def calc_entropy(self):
        
        ep = self.total_p / (self.total_n + self.total_p)
        en = self.total_n / (self.total_n + self.total_p)
        if ep == 0:
            if en == 0:
                self.entropy = 0
            else:
                self.entropy = -en * math.log2(en)
        else:
            if en == 0:
                self.entropy = -ep * math.log2(ep)
            else:
                self.entropy = -ep * math.log2(ep) - en * math.log2(en)

        for i in self.head.values():
            i.calc_entropy(self.total_n + self.total_p, self.entropy)

    def treeify(self,name=''):
        max = 0
        sel = None
        act_nodes = self.nodes
        aux_nodes = list()
        if name != '':
            aux_fit = dict()
            for x in name.split('|'):
                if x != '':                    
                    aux_fit[x.split(':')[0]] = x.split(':')[1]
            
            for y in act_nodes:
                if y.fit(aux_fit) :
                    aux_nodes.append(y)
            self.complete(aux_nodes)
            aux_name_l = name.split('|')
            aux_name = aux_name_l[len(aux_name_l)-2].split(':')
            self.act_node = self.head[aux_name[0]].atribs.get(aux_name[1])
        for i in self.head.values():
            if not i.used:
                for j in i.atribs.values():
                    if j.gain > max:
                        max = j.gain
                        sel = i
        if max == 0:
            return True
        sel.used = True
        if self.root == None:
            self.root = sel
        else:
            self.act_node.ret = sel
        for j in sel.atribs.values():
            if j.n == 0:
                j.ret = True
            elif j.p == 0:
                j.ret = False
            else:
                self.check.append(name+sel.name+':'+j.name+'|')
        if len(self.check)>0: return self.treeify(self.check.pop(0))
        return True

    def predict(self, node:decision_node):
        for i in node.at.items():
            ret = self.head[i[0]].atribs[i[1]].ret
            if(ret == True or ret == False):
                return ret
        return None



    
# class decision_node_f:

#     def __init__(self,name) -> None:
#         self.name = name


# class decision:

#     def __init__(self) -> None:
#         self.tree = 0

#     def play(self,value):
#         for i in self.tree:
#             i.name


#     def generate_tree(self, nodes,head):


