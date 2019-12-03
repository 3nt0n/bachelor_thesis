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




#### Mujoco Modeling (when everything works) 

http://www.mujoco.org/book/modeling.html

```bash

Summary:

Introduction:  
 Loading models:   
   Can load Xml into MJCF or URDF format with mj_loadXML  
   Top-level element is mujoco for MJCF and robot for URDF
   
 Compiling models:   
   Compiled into mjModel. Loading and Compiling are currently combined in one step

 Saving models:  
   mjModel can be saved into binary MJB with mj_saveModel  
   (also possible to save as MJCF with mj_saveLastXML)
   
   
MJCF Mechanisms:  
 Kinematic tree:  
   Main part of MJCF file is XML tree with nested body elements.  
   Top-level body is called worldbody.  
   A joint allows degree of freedoms between parent and child body
   
 Default settings:  
   You can set default values at the start.  
   You can define unlimited default classes.
   
   Example: 
     <mujoco>
      <default class="main">
          <geom rgba="1 0 0 1"/>
          <default class="sub">
              <geom rgba="0 1 0 1"/>
          </default>
      </default>

      <worldbody>
          <geom type="box"/>
          <body childclass="sub">
              <geom type="ellipsoid"/>
              <geom type="sphere" rgba="0 0 1 0"/>
              <geom type="cylinder" class="main"/>
          </geom>
      </worldbody>
    </mujoco>
 
 
  Coordinate frames:   
    There are global and local coordinates.
    
    Example (global):
   <body>
      <geom type="box" pos="1 0 0" size="0.5 0.5 0.5"/>
   </body>
   
   
  Frame orientations:  
    Spatial frames attributes:  
      quat : real(4), "1 0 0 0"  
      axisangle : real(4), optional  
      euler : real(3), optional  
      xyaxes : real(6), optional  
      zaxis : real(3), optional

  Solver parameters:  
     #TODO  
     solimp : real(5), "0.9 0.95 0.001 0.5 2"  
     solref : real(2), "0.02 1"

  Contact parameters:  
     geom pair can be explicitly defined with the XML element 'pair'.  
     Parameters:  
        condim - higher priority of two geoms condim is used. If same priority then maximum of oth condims  
        friction - contacts can have up to 5 friction coefficients, but geoms can only have 3. Higher priority geoms friction is used  
        margin,gap - maximum of those is used  
        solref, solimp - higher priority geoms is used. If same priority then weighted average is used
        
  Contact override:  
     override attribute of flag enables/disables this mechanism.  
     o_margin, o_solref, o_solimp attributes of option specify new solver parameters
     
  User parameters:  
     Some MJCF elements have the optional attribute user
        
```


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



https://github.com/openai/baselines/issues/622


## Issues

I had problems because my PC was too old and didn't support AVX instructions (Intel i3 graphic cards and newer needed)


## Notes



## Gym Fetch Tree

```bash

gym  
  setup.py  
  gym  
    core.py  
    error.py  
    logger.py  
    version.py  
    __init__.py  
    envs  
      registration.py  
      __init__.py  
      robotics  
        utils.py  
        rotations.py (??)  
        robot_env.py  
        fetch_env.py  
        __init__.py  
        assets  
          fetch  
            robot.xml  
            shared.xml  
            reach.xml  
            push.xml  
            slide.xml  
            pick_and_place.xml  
          stl  
            base_link_collision.stl            
            bellows_link_collision.stl         
            elbow_flex_link_collision.stl      
            estop_link.stl                     
            forearm_roll_link_collision.stl    
            gripper_link.stl                   
            head_pan_link_collision.stl        
            head_tilt_link_collision.stl       
            laser_link.stl  
            l_wheel_link_collision.stl  
            r_wheel_link_collision.stl  
            shoulder_lift_link_collision.stl  
            shoulder_pan_link_collision.stl  
            torso_fixed_link.stl  
            torso_lift_link_collision.stl  
            upperarm_roll_link_collision.stl  
            wrist_flex_link_collision.stl  
            wrist_roll_link_collision.stl              
        fetch  
          reach.py  
          push.py  
          slide.py  
          pick_and_place.py  


```




## Useful links

Paper: Basketball throw - https://www.ias.informatik.tu-darmstadt.de/uploads/Teaching/RobotLearningProject/Michels_Hochlaender_PPRL_2013.pdf



