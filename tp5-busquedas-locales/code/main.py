
from board import board;

from genetic import genetic;



b = board(6)
# b.hill_climb(0)
# b.sim_ann(0)
# print(b)

g = genetic(6)

g.seleccion_ga()

# print(b.get_mapa())

# print(b)

# for i in range(50):
#     print(b.get_mapa())

#     print(b)