import os
import parallelHillclimber as p
import numpy as np
import random

# Sets the random seed
np.random.seed(28)
random.seed(28)

# Runs the robot (if evolved, the fitness function will evolve based on the negative x direction)
hc = p.PARALLEL_HILL_CLIMBER()
hc.Evolve()