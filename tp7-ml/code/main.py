
import csv
from os import read
from decision_tree import *
import math


# target = "tennis"

attributes = []

file = open('/home/gx23/FAC/IA I/github/ia-uncuyo-2021/tp7-ml/code/tennis.csv')
reader = csv.reader(file, delimiter=',')
# Get attributes from csv
# print(reader)
attributes = next(reader)
print(attributes)

nodes = list()
for row in reader:
    print(row)
    nodes.append(decision_node(row))
    # print(decision_node(row))

# for i in nodes:
#     print(i)

dt = decision_tree(nodes,attributes)

print(dt)
ex_row = ['sunny', 'mild', 'high', 'true', 'yes']
ex = decision_node(ex_row)
ex_row2 = ['sunny', 'mild', 'high', 'false', 'yes']
ex2 = decision_node(ex_row)

print(dt.predict(ex))
print(dt.predict(ex2))


