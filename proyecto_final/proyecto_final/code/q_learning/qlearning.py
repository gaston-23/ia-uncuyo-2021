import numpy as np
import gym
import snake_env_q as senv
import time
import json

class data_collected:
    def __init__(self,episode,reward,time):
        self.episode = episode
        self.reward = reward
        self.time = time
    
    def __str__(self) -> str:
        res = 'Ep : '+str(self.episode)+' | '+str(self.reward)+' puntos en '+str(self.time)+' seg.'
        return res
        

env = senv.Snake()
n_observations = env.observation_space.n
n_actions = env.action_space.n


Q_table = dict()

#number of episode we will run
n_episodes = 700

#initialize the exploration probability to 1
exploration_proba = 1

#exploartion decreasing decay for exponential decreasing
exploration_decreasing_decay = 0.005

# minimum of exploration proba
min_exploration_proba = 0.01

#discounted factor
gamma = 0.95

#learning rate
lr = 0.00025

rewards_per_episode = list()

#we iterate over episodes
for e in range(n_episodes):
    start = time.time()
    #we initialize the first state of the episode
    current_state = env.reset()
    done = False
    score = 0
    #sum the rewards that the agent gets from the environment
    total_episode_reward = 0
    # print('episode ',e)
    while(not done): 
        # we sample a float from a uniform distribution over 0 and 1
        # if the sampled flaot is less than the exploration proba
        #     the agent selects arandom action
        # else
        #     he exploits his knowledge using the bellman equation 
        
        if np.random.uniform(0,1) < exploration_proba or not isinstance(Q_table.get(current_state),np.zeros(2).__class__):
            action = env.action_space.sample()
        else:
            action = np.argmax(Q_table[current_state])
            # action = np.argmax(Q_table[current_state,:])
        
        # The environment runs the chosen action and returns
        # the next state, a reward and true if the epiosed is ended.
        next_state, reward, done, new_score = env.step(action)

        if(not isinstance(Q_table.get(current_state),np.zeros(2).__class__)):
            Q_table[current_state] = np.zeros(n_actions)
        
        # We update our Q-table using the Q-learning iteration
        if(not isinstance(Q_table.get(next_state),np.zeros(2).__class__)):
            Q_table[next_state] = np.zeros(n_actions) 
        Q_table[current_state][action] = (1-lr) * Q_table[current_state][action] +lr*(reward + gamma*Q_table[next_state][action])


        # Q_table[current_state, action] = (1-lr) * Q_table[current_state, action] +lr*(reward + gamma*max(Q_table[next_state,:]))
        total_episode_reward = total_episode_reward + reward
        # If the episode is finished, we leave the for loop
        if not done:
            score = new_score

        
        current_state = next_state
    end = time.time()
    
    #We update the exploration proba using exponential decay formula 
    exploration_proba = max(min_exploration_proba, np.exp(-exploration_decreasing_decay*e))
    # rewards_per_episode.append(total_episode_reward)
    dc = data_collected(e,score,end-start)
    rewards_per_episode.append(dc)
    print(dc.__dict__)


print("Mean reward per  episodes")
data_dump = dict()
for i in range(n_episodes):
    data_dump [i] = rewards_per_episode[i].__dict__
    # print("life ",(i+1),": mean espiode reward: ",
        # np.mean(rewards_per_episode[i:(i+1)])) 
print(data_dump)
out_file = open("./output_q.json", "w") 
    
json.dump(data_dump, out_file, indent = 2) 
    
out_file.close() 

data_dump_q = dict()
for i in Q_table:
    data_dump_q [i] = Q_table[i].tolist()
    print("i: ",i,": mean espiode reward: ",Q_table[i].tolist())
        # np.mean(rewards_per_episode[i:(i+1)])) 
out_file_q = open("./output_q_table.json", "w") 
    
json.dump(data_dump_q, out_file_q, indent = 2) 
    
out_file_q.close() 
