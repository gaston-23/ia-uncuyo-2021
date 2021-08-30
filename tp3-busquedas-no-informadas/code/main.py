
from environment import environment
from agent import agent

test_map = '''|   |   |   |   |   | X | S |   | X | X |
            |   |   |   |   |   |   |   |   | X | X |
            |   |   |   |   | X |   |   |   |   | X |
            |   | X |   | X | X |   |   | X |   |   |
            |   | X |   |   | X |   |   |   |   |   |
            |   | X |   | O |   |   |   |   |   | X |
            | X |   | X | X |   |   |   |   |   |   |
            | X | X |   | X |   |   | X |   |   |   |
            |   | X |   |   |   | X |   |   |   | X |
            |   |   |   |   |   |   |   | X | X | X |'''

t = environment(testing=test_map)


print(t)

a = agent(t)

x = a.calcula_unif()

print(x.camino())


# print(test_map.split("\n")[1])

# for i in test_map.split("\n"):
#     # print(i.strip())
#     for j in i.split("| "):
#         print(j.strip(" |"))
# for i in range(3,len(test_map),4) :
#     print(test_map[i-1]+"---"+test_map[i])