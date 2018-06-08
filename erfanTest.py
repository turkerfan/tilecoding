import representation
import numpy as np

min_d0, min_d1, min_d2 = 0, 0, 0
max_d0, max_d1, max_d2 = 1, 1, 1

state_range = [[min_d0, min_d1, min_d2], [max_d0, max_d1, max_d2]]


# random_offsets = [-1.0/num_tiles[:,None] * np.random.rand(num_tiles.shape[0], num_tilings)
# 					for num_tiles, num_tilings in zip(ntiles, ntilings)]

tc = representation.TileCoding(input_indices = [np.arange(3)],
						ntiles = [100],
						ntilings = [2],
						hashing = None,
						state_range = state_range,
						rnd_stream = np.random.RandomState())
print(tc(np.array([0.1,0.1,0.2])))