# DEPRECATED, use baselines.common.plot_util instead

import os
import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns; sns.set()
import glob2
import argparse


def smooth_reward_curve(x, y):
    halfwidth = int(np.ceil(len(x) / 60))  # Halfwidth of our smoothing convolution
    k = halfwidth
    xsmoo = x
    ysmoo = np.convolve(y, np.ones(2 * k + 1), mode='same') / np.convolve(np.ones_like(y), np.ones(2 * k + 1),
        mode='same')
    return xsmoo, ysmoo


def load_results(file):
    if not os.path.exists(file):
        return None
    with open(file, 'r') as f:
        lines = [line for line in f]
    if len(lines) < 2:
        return None
    keys = [name.strip() for name in lines[0].split(',')]
    data = np.genfromtxt(file, delimiter=',', skip_header=1, filling_values=0.)
    if data.ndim == 1:
        data = data.reshape(1, -1)
    assert data.ndim == 2
    assert data.shape[-1] == len(keys)
    result = {}
    for idx, key in enumerate(keys):
        result[key] = data[:, idx]
    return result


def pad(xs, value=np.nan):
    maxlen = np.max([len(x) for x in xs])

    padded_xs = []
    for x in xs:
        if x.shape[0] >= maxlen:
            padded_xs.append(x)

        padding = np.ones((maxlen - x.shape[0],) + x.shape[1:]) * value
        x_padded = np.concatenate([x, padding], axis=0)
        assert x_padded.shape[1:] == x.shape[1:]
        assert x_padded.shape[0] == maxlen
        padded_xs.append(x_padded)
    return np.array(padded_xs)



#-----------------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str)
#add arguments for each plot used
parser.add_argument('dir2', type=str)
parser.add_argument('dir3', type=str)
parser.add_argument('--smooth', type=int, default=1)
args = parser.parse_args()





# Load all data.
data = {}
paths = [os.path.abspath(os.path.join(path, '..')) for path in glob2.glob(os.path.join(args.dir, '**', 'progress.csv'))]
for curr_path in paths:
    if not os.path.isdir(curr_path):
        continue
    results = load_results(os.path.join(curr_path, 'progress.csv'))
    if not results:
        print('skipping {}'.format(curr_path))
        continue
    print('loading {} ({})'.format(curr_path, len(results['epoch'])))
    with open(os.path.join(curr_path, 'params.json'), 'r') as f:
        params = json.load(f)
    success_rate = np.array(results['test/success_rate'])
    epoch = np.array(results['epoch']) + 1
    env_id = params['env_name']
    replay_strategy = params['replay_strategy']

    if replay_strategy == 'future':
        config = 'her'
    else:
        config = 'ddpg'
    if 'Dense' in env_id:
        config += '-dense'
    else:
        config += '-sparse'
    env_id = env_id.replace('Dense', '')

    # Process and smooth data.
    assert success_rate.shape == epoch.shape
    x = epoch
    y = success_rate
    if args.smooth:
        x, y = smooth_reward_curve(epoch, success_rate)
    assert x.shape == y.shape

    if env_id not in data:
        data[env_id] = {}
    if config not in data[env_id]:
        data[env_id][config] = []
    data[env_id][config].append((x, y))


#anton, copied 2x , data2, paths2, curr_path2, x2, y2, params2, success_rate2, epoch2, env_id2, replay_strategy2, config2
data2 = {}
paths2 = [os.path.abspath(os.path.join(path, '..')) for path in glob2.glob(os.path.join(args.dir2, '**', 'progress.csv'))]
for curr_path2 in paths2:
    if not os.path.isdir(curr_path2):
        continue
    results = load_results(os.path.join(curr_path2, 'progress.csv'))
    if not results:
        print('skipping {}'.format(curr_path2))
        continue
    print('loading {} ({})'.format(curr_path2, len(results['epoch'])))
    with open(os.path.join(curr_path2, 'params.json'), 'r') as f:
        params2 = json.load(f)
    success_rate2 = np.array(results['test/success_rate'])
    epoch2 = np.array(results['epoch']) + 1
    env_id2 = params2['env_name']
    replay_strategy2 = params2['replay_strategy']

    if replay_strategy == 'future':
        config2 = 'her'
    else:
        config2 = 'ddpg'
    if 'Dense' in env_id2:
        config2 += '-dense'
    else:
        config2 += '-sparse'
    env_id2 = env_id2.replace('Dense', '')

    # Process and smooth data.
    assert success_rate2.shape == epoch2.shape
    x2 = epoch2
    y2 = success_rate2
    if args.smooth:
        x2, y2 = smooth_reward_curve(epoch2, success_rate2)
    assert x2.shape == y2.shape

    if env_id2 not in data2:
        data2[env_id2] = {}
    if config2 not in data2[env_id2]:
        data2[env_id2][config2] = []
    data2[env_id2][config2].append((x2, y2))


#anton, copied 3x , data3, paths3, curr_path3, x3, y3, params3, success_rate3, epoch3, env_id3, replay_strategy3, config3
data3 = {}
paths3 = [os.path.abspath(os.path.join(path, '..')) for path in glob2.glob(os.path.join(args.dir3, '**', 'progress.csv'))]
for curr_path3 in paths3:
    if not os.path.isdir(curr_path3):
        continue
    results = load_results(os.path.join(curr_path3, 'progress.csv'))
    if not results:
        print('skipping {}'.format(curr_path3))
        continue
    print('loading {} ({})'.format(curr_path3, len(results['epoch'])))
    with open(os.path.join(curr_path3, 'params.json'), 'r') as f:
        params3 = json.load(f)
    success_rate3 = np.array(results['test/success_rate'])
    epoch3 = np.array(results['epoch']) + 1
    env_id3 = params3['env_name']
    replay_strategy3 = params3['replay_strategy']

    if replay_strategy == 'future':
        config3 = 'her'
    else:
        config3 = 'ddpg'
    if 'Dense' in env_id3:
        config3 += '-dense'
    else:
        config3 += '-sparse'
    env_id3 = env_id3.replace('Dense', '')

    # Process and smooth data.
    assert success_rate3.shape == epoch3.shape
    x3 = epoch3
    y3 = success_rate3
    if args.smooth:
        x3, y3 = smooth_reward_curve(epoch3, success_rate3)
    assert x3.shape == y3.shape

    if env_id3 not in data3:
        data3[env_id3] = {}
    if config3 not in data3[env_id3]:
        data3[env_id3][config3] = []
    data3[env_id3][config3].append((x3, y3))



#-----------------------------------------------------------------------------------------

# Plot data.
for env_id in sorted(data.keys()):
    print('exporting {}'.format(env_id))
    plt.clf()

    for config in sorted(data[env_id].keys()):
        xs, ys = zip(*data[env_id][config])
        xs, ys = pad(xs), pad(ys)
        assert xs.shape == ys.shape

#anton copied 2x

for env_id2 in sorted(data2.keys()):
    print('exporting {}'.format(env_id2))
    plt.clf()

    for config2 in sorted(data2[env_id2].keys()):
        xs2, ys2 = zip(*data2[env_id2][config2])
        xs2, ys2 = pad(xs2), pad(ys2)
        assert xs2.shape == ys2.shape


#anton copied 3x

for env_id3 in sorted(data3.keys()):
    print('exporting {}'.format(env_id3))
    plt.clf()

    for config3 in sorted(data3[env_id3].keys()):
        xs3, ys3 = zip(*data3[env_id3][config3])
        xs3, ys3 = pad(xs3), pad(ys3)
        assert xs3.shape == ys3.shape

#-----------------------------------------------------------------------------------------------

#add plt.plots, change "label = config" to what it should be named
        plt.plot(xs[0], np.nanmedian(ys, axis=0), label=config)
        plt.fill_between(xs[0], np.nanpercentile(ys, 25, axis=0), np.nanpercentile(ys, 75, axis=0), alpha=0.25)

#anton copied 2
        plt.plot(xs2[0], np.nanmedian(ys2, axis=0), label=config)
        plt.fill_between(xs2[0], np.nanpercentile(ys2, 25, axis=0), np.nanpercentile(ys2, 75, axis=0), alpha=0.25)

#anton copied 3
        plt.plot(xs3[0], np.nanmedian(ys3, axis=0), label=config)
        plt.fill_between(xs3[0], np.nanpercentile(ys3, 25, axis=0), np.nanpercentile(ys3, 75, axis=0), alpha=0.25)


#change title to what is needed
    plt.title(env_id)
    plt.xlabel('Epoch')
    plt.ylabel('Median Success Rate')
    plt.legend()
    plt.savefig(os.path.join(os.getcwd(), 'fig_{}.png'.format(env_id)))
