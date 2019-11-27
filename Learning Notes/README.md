# Notes

I am using Linux Ubuntu 16.04

python 3.5.2
Tensorflow 1.14.0
Mujoco200
mujoco-py 2.0.2.5
gym 0.14.0
baselines 0.1.6





## Machine Learning









## Reinforcement Learning
















## Tools/Setup

- A few tutorials which didn't work 100% for me anymore, the might still be helpful

https://github.com/openai/mujoco-py
https://github.com/reinforcement-learning-kr/pg_travel/wiki/Installing-Mujoco-py-on-Linux
https://www.tensorflow.org/install/pip?lang=python3




### Mujoco

#### Mujoco License

Get a test license (30-days) first

https://www.roboti.us/license.html

**(Test first if everythong works and only get the student license (free) after 30 days if everything worked.)**


#### Mujoco Download

Download the newest Mujoco https://www.roboti.us/index.html

Make a new folder ~/.mujoco and put extract the downloaded Mujoco Folder inside it

Put the mjkex.txt (your license) in the right folder (I am not sure where you have to put it, I copied and put it everywhere)

Test if mujoco works: go into the folder .mujoco/mujoco200/bin/ and try to run "./simulate ../model/humanoid.xml" in the terminal. 
You need need to run "chmod +x simulate" first to get the permission to execute it.

#### Set up your virtual environment

**A virtual environment helps you separate and use different versions of python etc. .You might need a different version for your machine learning projects than for your pc, so you can use a virtual environment for your project. A virtual environment doesn't take much memory, it just uses the version you specified. 
Example: When I run "python" in terminal , I get python 2.7, but when I run "python" in my VE, I get python 3.5**


( https://www.tensorflow.org/install/pip?lang=python3 )

install python3, pip, virtualenv if needed.

Create your virtual environment by running "virtualenv --system-site-packages -p python3 ./'yourenvironmentname'"

You can activate your VE by running "workon 'your environmentname'" and stop it by running "deactivate" in terminal.

Use "pip list" to get a list of your programs and version, use pip install "..." to install something

Now install everything following now in your virtual environment and only work in there.


#### Install tensorflow

run "pip install tensorflow" (maybe check which version you need)


#### Install mujoco-py

Go to the mujoco-py website to check if there are instructions (this guide might be too old):
https://github.com/openai/mujoco-py

run where you want to have the mujoco-py folder "git clone https://github.com/openai/mujoco-py.git" in terminal to get the folder.
Then go to the folder with cd "mujoco-py"
optionally run "pip install -r requirements.txt" and "pip install -r requirements.dev.txt" to install requirements.
Then run "python setup.py install" to install python-py

Test if it worked: just run "python" in terminal and then run "import mujoco-py" in python. I just some files are generated and there are no errors, then it should be working


### OpenAI



#### OpenAI - Gym
 
 Installing: https://github.com/openai/gym
 
 
 In Terminal: 
 
 git clone https://github.com/openai/gym.git
 cd gym
 pip install -e .
 
 
 
 
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
 
 
 
 
 



#### OpenAI - Baselines

Installing: https://github.com/openai/baselines


 In Terminal: 
 
 git clone https://github.com/openai/baselines.git
 cd baselines
 pip install -e .






## Issues

I had problems because my PC was too old and didn't support AVX instructions (Intel i3 graphic cards and newer needed)


## Notes


## Useful links

Paper: Basketball throw - https://www.ias.informatik.tu-darmstadt.de/uploads/Teaching/RobotLearningProject/Michels_Hochlaender_PPRL_2013.pdf



