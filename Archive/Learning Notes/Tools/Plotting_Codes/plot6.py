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
parser.add_argument('dir4', type=str)
parser.add_argument('dir5', type=str)
parser.add_argument('dir6', type=str)
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



#anton, copied 4x , data4, paths4, curr_path4, x4, y4, params4, success_rate4, epoch4, env_id4, replay_strategy4, config4
data4 = {}
paths4 = [os.path.abspath(os.path.join(path, '..')) for path in glob2.glob(os.path.join(args.dir4, '**', 'progress.csv'))]
for curr_path4 in paths4:
    if not os.path.isdir(curr_path4):
        continue
    results = load_results(os.path.join(curr_path4, 'progress.csv'))
    if not results:
        print('skipping {}'.format(curr_path4))
        continue
    print('loading {} ({})'.format(curr_path4, len(results['epoch'])))
    with open(os.path.join(curr_path4, 'params.json'), 'r') as f:
        params4 = json.load(f)
    success_rate4 = np.array(results['test/success_rate'])
    epoch4 = np.array(results['epoch']) + 1
    env_id4 = params4['env_name']
    replay_strategy4 = params4['replay_strategy']

    if replay_strategy == 'future':
        config4 = 'her'
    else:
        config4 = 'ddpg'
    if 'Dense' in env_id4:
        config4 += '-dense'
    else:
        config4 += '-sparse'
    env_id4 = env_id4.replace('Dense', '')

    # Process and smooth data.
    assert success_rate4.shape == epoch4.shape
    x4 = epoch4
    y4 = success_rate4
    if args.smooth:
        x4, y4 = smooth_reward_curve(epoch4, success_rate4)
    assert x4.shape == y4.shape

    if env_id4 not in data4:
        data4[env_id4] = {}
    if config4 not in data4[env_id4]:
        data4[env_id4][config4] = []
    data4[env_id4][config4].append((x4, y4))


#anton, copied 5x , data5, paths5, curr_path5, x5, y5, params5, success_rate5, epoch5, env_id5, replay_strategy5, config5
data5 = {}
paths5 = [os.path.abspath(os.path.join(path, '..')) for path in glob2.glob(os.path.join(args.dir5, '**', 'progress.csv'))]
for curr_path5 in paths5:
    if not os.path.isdir(curr_path5):
        continue
    results = load_results(os.path.join(curr_path5, 'progress.csv'))
    if not results:
        print('skipping {}'.format(curr_path5))
        continue
    print('loading {} ({})'.format(curr_path5, len(results['epoch'])))
    with open(os.path.join(curr_path5, 'params.json'), 'r') as f:
        params5 = json.load(f)
    success_rate5 = np.array(results['test/success_rate'])
    epoch5 = np.array(results['epoch']) + 1
    env_id5 = params5['env_name']
    replay_strategy5 = params5['replay_strategy']

    if replay_strategy == 'future':
        config5 = 'her'
    else:
        config5 = 'ddpg'
    if 'Dense' in env_id5:
        config5 += '-dense'
    else:
        config5 += '-sparse'
    env_id5 = env_id5.replace('Dense', '')

    # Process and smooth data.
    assert success_rate5.shape == epoch5.shape
    x5 = epoch5
    y5 = success_rate5
    if args.smooth:
        x5, y5 = smooth_reward_curve(epoch5, success_rate5)
    assert x5.shape == y5.shape

    if env_id5 not in data5:
        data5[env_id5] = {}
    if config5 not in data5[env_id5]:
        data5[env_id5][config5] = []
    data5[env_id5][config5].append((x5, y5))



#anton, copied 6x , data6, paths6, curr_path6, x6, y6, params6, success_rate6, epoch6, env_id6, replay_strategy6, config6
data6 = {}
paths6 = [os.path.abspath(os.path.join(path, '..')) for path in glob2.glob(os.path.join(args.dir6, '**', 'progress.csv'))]
for curr_path6 in paths6:
    if not os.path.isdir(curr_path6):
        continue
    results = load_results(os.path.join(curr_path6, 'progress.csv'))
    if not results:
        print('skipping {}'.format(curr_path6))
        continue
    print('loading {} ({})'.format(curr_path6, len(results['epoch'])))
    with open(os.path.join(curr_path6, 'params.json'), 'r') as f:
        params6 = json.load(f)
    success_rate6 = np.array(results['test/success_rate'])
    epoch6 = np.array(results['epoch']) + 1
    env_id6 = params6['env_name']
    replay_strategy6 = params6['replay_strategy']

    if replay_strategy == 'future':
        config6 = 'her'
    else:
        config6 = 'ddpg'
    if 'Dense' in env_id6:
        config6 += '-dense'
    else:
        config6 += '-sparse'
    env_id6 = env_id6.replace('Dense', '')

    # Process and smooth data.
    assert success_rate6.shape == epoch6.shape
    x6 = epoch6
    y6 = success_rate6
    if args.smooth:
        x6, y6 = smooth_reward_curve(epoch6, success_rate6)
    assert x6.shape == y6.shape

    if env_id6 not in data6:
        data6[env_id6] = {}
    if config6 not in data6[env_id6]:
        data6[env_id6][config6] = []
    data6[env_id6][config6].append((x6, y6))


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


#anton copied 4x

for env_id4 in sorted(data4.keys()):
    print('exporting {}'.format(env_id4))
    plt.clf()

    for config4 in sorted(data4[env_id4].keys()):
        xs4, ys4 = zip(*data4[env_id4][config4])
        xs4, ys4 = pad(xs4), pad(ys4)
        assert xs4.shape == ys4.shape


#anton copied 6x

for env_id6 in sorted(data6.keys()):
    print('exporting {}'.format(env_id6))
    plt.clf()

    for config6 in sorted(data6[env_id6].keys()):
        xs6, ys6 = zip(*data6[env_id6][config6])
        xs6, ys6 = pad(xs6), pad(ys6)
        assert xs6.shape == ys6.shape



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

#anton copied 4
        plt.plot(xs4[0], np.nanmedian(ys4, axis=0), label=config)
        plt.fill_between(xs4[0], np.nanpercentile(ys4, 25, axis=0), np.nanpercentile(ys4, 75, axis=0), alpha=0.25)

#anton copied 5
        plt.plot(xs5[0], np.nanmedian(ys5, axis=0), label=config)
        plt.fill_between(xs5[0], np.nanpercentile(ys5, 25, axis=0), np.nanpercentile(ys5, 75, axis=0), alpha=0.25)

#anton copied 6
        plt.plot(xs6[0], np.nanmedian(ys6, axis=0), label=config)
        plt.fill_between(xs6[0], np.nanpercentile(ys6, 25, axis=0), np.nanpercentile(ys6, 75, axis=0), alpha=0.25)


#change title to what is needed
    plt.title(env_id)
    plt.xlabel('Epoch')
    plt.ylabel('Median Success Rate')
    plt.legend()
    plt.savefig(os.path.join(os.getcwd(), 'fig_{}.png'.format(env_id)))
