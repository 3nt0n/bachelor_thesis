# Notes

I am using Linux Ubuntu 16.04

## Machine Learning









## Reinforcement Learning
















## Tools/Setup

- A few tutorials which didn't work 100% for me anymore, the might still be helpful

https://github.com/openai/mujoco-py
https://github.com/reinforcement-learning-kr/pg_travel/wiki/Installing-Mujoco-py-on-Linux


## Mujoco

# Mujoco License

Get a test license (30-days) first

https://www.roboti.us/license.html

**(Test first if everythong works and only get the student license (free) after 30 days if everything worked.)**


# Mujoco Download

Download the newest Mujoco https://www.roboti.us/index.html

Make a new folder ~/.mujoco and put extract the downloaded Mujoco Folder inside it

Put the mjkex.txt (your license) in the right folder (I am not sure where you have to put it, I copied and put it everywhere)







## OpenAI

Installing: https://github.com/openai/gym

### OpenAI - Gym
 
 
 Create your own environment:
 https://github.com/openai/gym/blob/master/docs/creating-environments.md
 
 https://www.novatec-gmbh.de/en/blog/creating-a-gym-environment/
 https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e
 https://stackoverflow.com/questions/45068568/how-to-create-a-new-gym-environment-in-openai


 Running Environment in Python:
 
 import gym
 
 
 import gym_"customenv"
 
 
 env = gym.make("EnvName")
 

 env.reset()
 
 
 env.step(env.action_space.sample())
 
 
 env.render()
 
 
 env.close()
 
 
 
 
 



### OpenAI - Baselines










## Notes


## Useful links

Paper: Basketball throw - https://www.ias.informatik.tu-darmstadt.de/uploads/Teaching/RobotLearningProject/Michels_Hochlaender_PPRL_2013.pdf
