from gym.envs.registration import registry, register, make, spec


# Robotics
# ----------------------------------------

def _merge(a, b):
    a.update(b)
    return a

for reward_type in ['sparse', 'dense']:
    suffix = 'Dense' if reward_type == 'dense' else ''
    kwargs = {
        'reward_type': reward_type,
    }

    #by Anton Mai

    register(
        id='FetchToss{}-v0'.format(suffix),
        entry_point='gym_toss.envs:FetchTossEnv',
        kwargs=kwargs,
        max_episode_steps=50,
    )

