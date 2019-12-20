

## Experiments


Here are different self-made environments documented.

Also training and plots.

You should be able to run the trained models if you download it.



## Todo

Check out how to make plots visible in this README.md and make a nice structure for the test results in this README.md




##Todo

Step 1: Standard Parameters for Fetch Slide








Step 2: Change Parameters for Fetch Slide (and use a ball)


Versions:

-Slideball-v0: Test environment




-Slideball-v1: Same as FetchSlide, but with ball
  --> the ball has some extra rotation which feels slightly unnatural. Not sure where it comes from. Maybe the friction ratio (between static, slide and roll friction) needs to be more precise
(trained 50ep)

-Slideball-v1.1: Same as version 1, but with 2 times more friction
(not trained yet, maybe later, needs more fine tuning before)

-Slideball-v2: Same as version 1, but doubled goal distance
(trained ~20ep/100k)

-Slideball-v3: Same as version 2, but with bigger goal
(not trained yet)

-Slideball-v4: Same as version 1, but make the goal as big as version 1 and 2 together

-Slideball-v5: 

-Slideball-last: have a natural rolling ball and a good size. have a decent distance (2-3 times) and make it trainable.




Step 3: Make Fetch Toss

- Do the same as for Slideball, but use FetchPickAndPlace (makes it use the gripper and puts goal in air)

- use the target0 in the xml file and put a basket like thing around it.
