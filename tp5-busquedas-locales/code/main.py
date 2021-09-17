
from board import board;
from time import time;
from genetic import genetic;
import pandas as pd;
from statistics import mean,stdev;


# b = board(8)
# b.hill_climb(0)
# b.sim_ann(0)
# print(b)

# g = genetic(8)

# g.seleccion_ga()

# print(b.get_mapa())

# print(b)

# for i in range(50):
#     print(b.get_mapa())

#     print(b)


qu = [4,8,10]
hc = {  'reinas': [],
        'pasos': [],
        'tiempo': []}
sa = {  'reinas': [],
        'pasos': [],
        'tiempo': []}
ga = {  'reinas': [],
        'pasos': [],
        'tiempo': []}

for q in range(len(qu)):
    for i in range(30):
        start = time()
        b = board(qu[q])
        iter =  b.hill_climb(0)
        end = time()
        if iter < 1000:
            prom = end - start
            hc.get('reinas').append(qu[q])
            hc.get('pasos').append(iter)
            hc.get('tiempo').append(prom)
    print("media_pasos hc:: ",mean(hc.get('pasos')))
    print("media_tiempo hc:: ",mean(hc.get('tiempo')))
    for i in range(30):
        start = time()
        b = board(qu[q])
        iter =  b.sim_ann(0)
        end = time()
        if iter < 1000:
            prom = end - start
            sa.get('reinas').append(qu[q])
            sa.get('pasos').append(iter)
            sa.get('tiempo').append(prom)
    print("media_pasos sa:: ",mean(sa.get('pasos')))
    print("media_tiempo sa:: ",mean(sa.get('tiempo')))

    for i in range(30):
        start = time()
        b = board(qu[q])
        iter =  b.sim_ann(0)
        end = time()
        if iter < 1000:
            prom = end - start
            sa.get('reinas').append(qu[q])
            sa.get('pasos').append(iter)
            sa.get('tiempo').append(prom)
    print("media_pasos sa:: ",mean(sa.get('pasos')))
    print("media_tiempo sa:: ",mean(sa.get('tiempo')))

df = pd.DataFrame(hc, columns = ['reinas', 'pasos', 'tiempo'])
df.to_csv('output_hc.csv')


    
