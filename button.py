import os
import parallelHillclimber as p

# Runs the robot (if evolved, the fitness function will evolve based on the negative x direction)
hc = p.PARALLEL_HILL_CLIMBER()
hc.Evolve()