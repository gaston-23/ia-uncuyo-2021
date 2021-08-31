
from environment import environment
from agent import agent
import statistics
import matplotlib.pyplot as plt

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

# t = environment(testing=test_map)


res = []

while len(res) < 30:
    e = environment()
    ag = agent(e)
    y = ag.calcula_star()
    if ag.eficiencia > 0 :
        res.append(ag.eficiencia)






print(res)
print("Media:",statistics.mean(res))
print("Desviación estandar:",statistics.stdev(res))
print("")



labels = ['BFS', 'DFS', 'Unif', 'A*']
 
medias = [3056.266666666667,3120.5333333333333,2373.366666666667,statistics.mean(res)]
 
plt.bar(labels, medias)
 
plt.ylabel('Media de estados')
 
plt.xlabel('Algoritmos')
 
plt.title('Media de estados recorridos por algoritmo')
 
plt.show()