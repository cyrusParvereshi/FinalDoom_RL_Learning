import gym  #https://gym.openai.com/
from gym import spaces
import numpy as np
def get_env_info(env):
	print(env.observation_space.high)
	print(env.observation_space.low)
	#print(env.action_space.n)


env = gym.make("MountainCar-v0")#"MountainCar-v0")
env.reset()

get_env_info(env)
DISCRETE_OBS_SIZE = [20] * len(env.observation_space.high) #observation size, not hard coded normally
print(DISCRETE_OBS_SIZE)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OBS_SIZE
print(discrete_os_win_size)
#q_table = np.random.uniform(low=-2, high=0,size=(DISCRETE_OBS_SIZE + [env.action_space.n]))
# print(q_table.shape)
done = False
counter = 0
while not done:
	counter +=1
	action = 1
	new_state, reward, done, _ = env.step(action)x
	print(reward, new_state)
	env.render()
print("Total steps: ", counter)
env.close()


