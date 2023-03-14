import os
import parallelHillclimber as p
import numpy as np
import random
import matplotlib.pyplot as plt
import constants as c
import runSim

# os.system("del brain*.nndf")
# os.system("del fitness*.txt")
# os.system("del body*.urdf")
# exit()

# Sets the random seed
np.random.seed(27)
random.seed(27)

fitnessDict = dict()
robotDict = dict()
# Runs the robot (if evolved, the fitness function will evolve based on the negative x direction)
for i in range(5):
    print("\nSeed: " + str(i))
    print("")
    hc = p.PARALLEL_HILL_CLIMBER()
    best, parent, fitness = hc.Evolve()
    fitnessDict[i] = fitness
    robotDict[i] = [best, parent]

# find best overall
bestFitness = 0
bestIndex = 0
for i in range(5):
    if fitnessDict[i][c.numberOfGenerations - 1] < bestFitness:
        bestFitness = fitnessDict[i][c.numberOfGenerations - 1]
        bestIndex = i

print("\nSeed: " + str(bestIndex) + ", Best Fitness: " + str(bestFitness) + ", ID: " + str(robotDict[bestIndex][0][4]) + ", Parent: " + str(robotDict[bestIndex][1][4]))
os.system("del brain*.nndf")
os.system("del fitness*.txt")
os.system("del body*.urdf")
# show best
runSim.Start_Simulation(robotDict[bestIndex][0], "GUI")
#  and parent of best
runSim.Start_Simulation(robotDict[bestIndex][1], "GUI")

# plot
for i in range(5):
    plt.plot(fitnessDict[i], label="Seed {}".format(i))
    # add labels and title to the plot
plt.xlabel('Generation')
plt.ylabel('Fitness (Distance in -x Direction)')
plt.title('Robot Seed VS Fitness')
plt.legend()
plt.show()