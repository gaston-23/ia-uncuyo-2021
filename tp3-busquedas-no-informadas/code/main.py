
from environment import environment
from agent import agent
import statistics

# test_map = '''|   |   |   |   |   | X | S |   | X | X |
#             |   |   |   |   |   |   |   |   | X | X |
#             |   |   |   |   | X |   |   |   |   | X |
#             |   | X |   | X | X |   |   | X |   |   |
#             |   | X |   |   | X |   |   |   |   |   |
#             |   | X |   | O |   |   |   |   |   | X |
#             | X |   | X | X |   |   |   |   |   |   |
#             | X | X |   | X |   |   | X |   |   |   |
#             |   | X |   |   |   | X |   |   |   | X |
#             |   |   |   |   |   |   |   | X | X | X |'''

test_map = '''|   |   | X |   |   | X |   |   |   |   |
            |   |   | X | X | X | S |   |   | X |   |
            |   |   |   |   | X |   | X |   | X | X |
            |   |   |   | O |   |   |   |   |   |   |
            |   |   |   |   |   |   | X | X | X |   |
            | X | X | X |   |   |   |   | X | X |   |
            |   |   |   | X |   |   |   |   |   |   |
            | X |   | X | X |   |   |   |   |   | X |
            | X |   | X |   | X |   |   | X |   |   |
            |   |   |   |   |   | X |   |   |   | X |'''

# t = environment(testing=test_map)
# t = environment()


# print(t)

# a = agent(t)

# x = a.calcula_BFS()

# print(x.camino())

# print(a.eficiencia)


res_B = []

while len(res_B) < 30:
    e_b = environment()
    ag_b = agent(e_b)
    y_b = ag_b.calcula_BFS()
    if ag_b.eficiencia > 0 :
        res_B.append(ag_b.eficiencia)

res_D = []

while len(res_D) < 30:
    
    e_d = environment()
    ag_d = agent(e_d)
    y_d = ag_d.calcula_DFS()
    if ag_d.eficiencia > 0 :
        res_D.append(ag_d.eficiencia)
    else:
        print(e_d)
        print(y_d.camino())
        break

res_U = []

while len(res_U) < 30:
    e_u = environment()
    ag_u = agent(e_u)
    y_u = ag_u.calcula_unif()
    if ag_u.eficiencia > 0 :
        res_U.append(ag_u.eficiencia)




print("BFS: ",res_B)
print("DFS: ",res_D)
print("uniforme: ",res_U)

print("Media_BFS:",statistics.mean(res_B))
print("Desviación estandar_BFS:",statistics.stdev(res_B))
print("")

print("Media_DFS:",statistics.mean(res_D))
print("Desviación estandar_DFS:",statistics.stdev(res_D))
print("")

print("Media_unif:",statistics.mean(res_U))
print("Desviación estandar_unif:",statistics.stdev(res_U))
print("")
