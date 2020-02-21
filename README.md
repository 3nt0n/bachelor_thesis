# bachelor_thesis


**Thesis_AntonMai:** the LateX files of my thesis

**Environments:** the gym and baselines folder for my environments FetchSlideball and FetchToss, and their versions

**Experiments:** Training data of the environments and plots.

**Videos,Plots:** The plots and videos (.mkv) for the experiments

------------------------------------------------------------------------



**Environments:**

 Standard Environments by OpenAI:

  -FetchReach-v1
  -FetchPush-v1
  -FetchSlide-v1
  -FetchPickAndPlace-v1

 FetchSlideball Environment:
 
  -FetchSlideball-v1: Same as FetchSlide, but with ball
  
  -FetchSlideball-v2: Same as FetchSlideball-v1, but with bigger distance

  -FetchSlideball-v3: Same as FetchSlideball-v2, but with 10% friction

  -FetchSlideball-v4: Same as FetchSlideball-v2, but with 50% friction

  -FetchSlideball-v6: Same as FetchSlideball-v2, but with 25% friction

 FetchToss Environment:

  -FetchPickAndPlaceball-v1: FetchPickAndPlace-v1, but with a ball

  -FetchToss-v1: Environment FetchPickAndPlaceball-v1 changed to contain a box and the goal is in the box.

  -FetchTosscube-v1: Same as FetchToss-v1, but with a cube

  -FetchToss-v4: Same as FetchToss-v1, but the weight is only 1%, the box was modified and friction was added (if the ball is thrown on the box instead of inside, it would have been staying still in v1)

-----------------------------------------------


Each except for FetchSlideball-v2 was trained for 50 epochs. following code was used for training:

mpirun -np 10 python -m baselines.run --alg=her --env=<environment> --num_env=2 --num_timesteps=<numberneededfor50epochs(usually250000)> --save_path=<savepath> --log_path=<logpath>

Plappert et. al used 19 CPUs in their paper instead of only 10.

----------------------------

**How to run the environments:**

Go to the Environments/gym folder and run "pip install -e ." in the terminal.
Then go to the Environments/baselines folder and also run "pip install -e ."

Then run "python -m baselines.run --alg=her --env=<environment> --num_timesteps=0 --load_path=<filepath> --play" to see the environment.

Example: To run FetchSlideball-v1, use "python -m baselines.run --alg=her --env=FetchSlideball-v1 --num_timesteps=0 --load_path=./Experiments/FetchSlideball-v1_training/250k-2env-10c/fetchslide-250k-2env-10c --play"






















