
from Environment import Environment
from Agent import Agent


test_env = [[2,2], [4,4], [8,8], [16,16], [32,32], [64,64], [128,128]]
dirt_p = [0.1, 0.2, 0.4, 0.8]

i = 6
k = 2
ran = 0
p = Environment(test_env[i][0],test_env[i][1],dirt_p[k])
a = Agent(0,0,p,p==1)
a.calcula()

print(test_env[i][0],test_env[i][1],dirt_p[k],ran==1, sep=" X ")
print(a.calcula_eficiencia()*100,"%")
print(a.limpios,p.suc_ini,sep="/")

