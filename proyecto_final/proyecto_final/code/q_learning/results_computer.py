from math import inf
import math
from turtle import st, width
from matplotlib import markers
import matplotlib.pyplot as plt

import json

import numpy as np


class data_collected:
    def __init__(self,episode,reward,time):
        self.episode = episode
        self.reward = reward
        self.time = time
    
    def __str__(self) -> str:
        res = 'Ep : '+str(self.episode)+' | '+str(self.reward)+' puntos en '+str(self.time)+' seg.'
        return res

def getMaxTime(data : list, human=True):
  acc = 0
  for k in range(len(data)):
    acc += data[k].time
  if human:
    return getHumanTime(acc)
  else:
    return acc

def getHumanTime(secs):
  h = secs // 3600
  m = int(((secs / 3600) - h) * 60)
  s = (((((secs / 3600) - h) * 60) - m) * 60) 
  return str(h) + 'h '+str(m)+' m '+str(s)+' s'

def getMaxScore(data: list):
  acc = 0
  maxV = 0
  for k in range(len(data)):
    curr = data[k].reward
    if(curr > maxV):
      maxV = curr
    acc += curr
  return acc,maxV


'''
  Obtiene la puntuacion y el tiempo acumulado para dicha puntuacion
'''
def getTriesXTime(data: list):
  tries = list()
  times = list()
  time_acc = 0
  for k in range(len(data)):
    time_acc += data[k].time
    tries.append(data[k].reward)    
    times.append(time_acc)  
  return tries,times

'''
  Obtiene el tiempo que tardo en conseguir cada puntuacion al menos 3 veces
'''
def getMaxScoreXTime(data: list,max_value: int):
  tries = np.array(np.zeros(max_value))
  times = np.array(np.zeros(max_value))
  # keys = np.array(np.zeros(max_value))
  # max_score = 0
  time_acc = 0
  for k in range(len(data)):
    curr = data[k].reward
    tries[curr] += 1
    time_acc += data[k].time
    if(tries[curr] < 4 ):
      times[curr] += time_acc
  for k in range(max_value):
    if(tries[curr] < 4 ):
      times[curr] = 0
    else:
      times[curr] = times[curr]/3
  return times

'''
  Obtiene cuantas veces obtuvo cada puntuacion
'''
def getTriesXScore(data: list,max_value: int):
  tries = np.array(np.zeros(max_value))
  
  for k in range(len(data)):
    curr = data[k].reward
    tries[curr] += 1
  return tries

'''
  Obtiene total de puntuacion ordenado
'''
def getScores(data: list):
  scores = list()
  
  for k in range(len(data)):
    scores.append(data[k].reward)
  scores.sort()
  return scores

'''
  tiempo transcurrido hasta una media, si se activa la opcion window, se puede limitar la ventana de registros a 5
'''
def timeToMean(data: list, mean_val: int,window =False):
  time_acc = 0
  values_acc = list()
  for k in range(len(data)):
    curr = data[k].reward
    values_acc.append(curr)
    time_acc += data[k].time
    mean_value = np.mean(np.array(values_acc))
    if(window and len(values_acc)>5):
      values_acc.pop(0)
    
    if(mean_value > mean_val ):
      return time_acc
  return inf

'''
  episodios transcurrido hasta una media, si se activa la opcion window, se puede limitar la ventana de registros a 5
'''
def epToMean(data: list, mean_val: int):
  values_acc = list()
  for k in range(len(data)):
    curr = data[k].reward
    values_acc.append(curr)
    mean_value = np.mean(np.array(values_acc))
    
    if(mean_value > mean_val ):
      return k
  return inf


    
q = list()
drl = list()
# Opening JSON file
with open('./output_q.json', 'r') as output_q:
  
    # Reading from json file
    json_object = json.load(output_q)

for k in json_object.keys():
  q.append(data_collected(int(k),json_object[k]['reward'],json_object[k]['time']))

with open('./output_drl.json', 'r') as output_drl:
  
    # Reading from json file
    json_object = json.load(output_drl)

for k in json_object.keys():
  drl.append(data_collected(int(k),json_object[k]['reward'],json_object[k]['time']))


(acc_q,max_q) = getMaxScore(q)
(acc_drl,max_drl) = getMaxScore(drl)

print('Tiempo total q_lear ' + getMaxTime(q)+ ' puntuacion max: '+str(max_q)+' puntuacion acc: '+str(acc_q))
print('Tiempo total dr_lear ' + getMaxTime(drl)+ ' puntuacion max: '+str(max_drl)+' puntuacion acc: '+str(acc_drl))

(tries_q,times_q) = getTriesXTime(q)
(tries_drl,times_drl) = getTriesXTime(drl)

# Plot Score vs Time to reached

plt.figure(1)
## Q learning 
plt.subplot(2,1,1)
plt.plot(times_q,tries_q, marker = 'o', color='#FD881A')
plt.xlabel('Time(seg)')
plt.ylabel('Max Score')
plt.title('Q ')


## Q learning 
plt.subplot(2,1,2)
plt.plot(times_drl,tries_drl, marker = 'o', color='#1A77FD')
plt.xlabel('Time(seg)')
plt.ylabel('Max Score')
plt.title('DRL')


# plt.show()

# Plot each Score vs mean Time to reach it

(times_q) = getMaxScoreXTime(q,max_q+1)
(times_drl) = getMaxScoreXTime(drl,max_drl+1)
# print(times_q)
# print(np.arange(0,(max_q+1)))
plt.figure(2)
## Q learning 
plt.subplot(2,1,1)
plt.bar(np.arange(0,(max_q+1)),times_q, color='#FD881A')
plt.ylabel('Time(seg)')
plt.xlabel('Max Score')
plt.title('Q')


## Q learning 
plt.subplot(2,1,2)
plt.bar(np.arange(0,(max_drl+1)),times_drl, color='#1A77FD')
plt.ylabel('Time(seg)')
plt.xlabel('Max Score')
plt.title('DRL ')


# plt.show()

# Box chart

fig = plt.figure(3)

box_q = getScores(q)
print('Q: '+str(np.mean(box_q)))
box_drl = getScores(drl)
print('DRL: '+str(np.mean(box_drl)))

data = [box_q,box_drl]

ax = fig.add_subplot(111)
 
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#FD881A', '#1A77FD']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# x-axis labels
ax.set_yticklabels(['Q', 'DRL'])
 
# Adding title
plt.title("Diagrama de cajas y bigotes para las puntuaciones de cada algoritmo")
 
# Removing top axes and right axes
# ticks
# ax.get_xaxis().tick_bottom()
# ax.get_yaxis().tick_left()
     
# show plot


# Tiempo hasta la media de 7

print ('Tiempo hasta la media de 7: ')
q_time = timeToMean(q,7)
drl_time = timeToMean(drl,7)
print('q: '+str(q_time)+' drl: '+str(drl_time))

y = [q_time,drl_time]
x = ['Q','DRL']

fig, ax = plt.subplots(figsize=(5, 3))
bars = ax.barh(x,y, 0.1, color=["#FD881A","#1A77FD"])
for bar in bars:
  width = bar.get_width() #Previously we got the height
  label_y_pos = bar.get_y() + bar.get_height() / 2
  ax.text(width, label_y_pos, s=f'{np.round(width,0)}'+' s', va='center')
for tick in ax.yaxis.get_major_ticks():
  tick.label.set_fontsize(14)

plt.title('Tiempo transcurrido hasta obtener una recompensa media de 7 (s)')


# Episodios hasta la media de 7

print ('Episodios hasta obtener una recompensa media de 7: ')
q_ep = epToMean(q,7)
drl_ep = epToMean(drl,7)
print('q: '+str(q_ep)+' drl: '+str(drl_ep))

y = [q_ep,drl_ep]
x = ['Q','DRL']

fig, ax = plt.subplots()
bars = ax.barh(x,y, 0.1, color=["#FD881A","#1A77FD"])
for bar in bars:
  width = bar.get_width() #Previously we got the height
  label_y_pos = bar.get_y() + bar.get_height() / 2
  ax.text(width, label_y_pos, s=f'{np.round(width,0)}'+' ep', va='center')
for tick in ax.yaxis.get_major_ticks():
  tick.label.set_fontsize(14)

plt.title('Episodios hasta obtener una recompensa media de 7')

# Max puntuacion

print ('Max puntuacion: ')

print('q: '+str(max_q)+' drl: '+str(max_drl))

y = [max_q,max_drl]
x = ['Q','DRL']

fig, ax = plt.subplots()
bars = ax.barh(x,y, 0.1, color=["#FD881A","#1A77FD"])
for bar in bars:
  width = bar.get_width() #Previously we got the height
  label_y_pos = bar.get_y() + bar.get_height() / 2
  ax.text(width, label_y_pos, s=f'{np.round(width,0)}'+' puntos', va='center')
for tick in ax.yaxis.get_major_ticks():
  tick.label.set_fontsize(14)

plt.title('Max puntuacion de cada algoritmo')

# Tiempo total

print ('Tiempo total: ')
q_tot_time = getMaxTime(q,False)
drl_tot_time = getMaxTime(drl,False)
print('q: '+str(q_tot_time)+' drl: '+str(drl_tot_time))

y = [q_tot_time,drl_tot_time]
x = ['Q','DRL']

fig, ax = plt.subplots()
bars = ax.barh(x,y, 0.1, color=["#FD881A","#1A77FD"])
for bar in bars:
  width = bar.get_width() #Previously we got the height
  label_y_pos = bar.get_y() + bar.get_height() / 2
  ax.text(width, label_y_pos, s=f'{np.round(width,0)}'+' s', va='center')
for tick in ax.yaxis.get_major_ticks():
  tick.label.set_fontsize(14)

plt.title('Tiempo total de cada algoritmo (s)')




plt.show()
