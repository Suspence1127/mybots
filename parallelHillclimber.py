import solution
import constants as c
import copy
import os
import runSim
import numpy
import random
import matplotlib.pyplot as plt
from addRemoveLink import robotMutation

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        self.fitnessDictParents = dict()
        self.fitnessDictChildren = dict()
        self.fitnessPlotData = [[0 for j in range(c.numberOfGenerations)] for i in range(c.populationSize)]
        self.curGen = 0
        self.parents = dict()
        self.nextAvailableID = 0
        for num in range(c.populationSize):
            self.parents[num] = solution.SOLUTION(self.nextAvailableID).Create_Simulation()
            self.nextAvailableID = self.nextAvailableID + 1
        self.ogParents = copy.deepcopy(self.parents)

    def Evolve(self):
        self.Evaluate(self.parents, True)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.Show_Best()
        pass

    def Show_Best(self):
        bestKey = 0
        for key in self.parents.keys():
            if self.fitnessDictParents[key] < self.fitnessDictParents[bestKey]:
                bestKey = key
        runSim.Start_Simulation(self.parents[bestKey], "GUI")
        runSim.Start_Simulation(self.ogParents[bestKey], "GUI")
        print("Best Fitness: " + str(self.fitnessDictParents[bestKey]) + ", ID: " + str(self.parents[bestKey][4]) + ", Parent: " + str(bestKey))

        for i in range(c.populationSize):
            plt.plot(self.fitnessPlotData[i], label="Robot {}".format(i))
        # add labels and title to the plot
        plt.xlabel('Generation')
        plt.ylabel('Fitness (Distance in -x Direction)')
        plt.title('Robot VS Fitness')
        plt.legend()
        plt.show()
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        pass

    def Spawn(self):
        # Robot = [self.linkDict, self.jointDict, self.linkSensor, self.synapseDict, self.myID, self.numLinks, self.actualNumLinks]
        self.children = dict()
        for key in self.parents.keys():
            newChild = copy.deepcopy(self.parents[key])
            newChild[4] = self.nextAvailableID
            self.children[key] = newChild
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for key in self.children:
            currChild = self.children[key]
            # Determines whether to remove a link, add a link, or change a sensor
            mutateNum = numpy.random.randint(3)
            # Change Random Sensor Weight
            if mutateNum == 0:
                newSynap = self.MutateSynapses(currChild[3])
                currChild[3] = newSynap
                self.children[key] = currChild
            # Add block
            elif mutateNum == 1:
                self.children[key] = robotMutation.addLink(currChild)
            # Remove block
            else:
                if currChild[6] > 3:
                    self.children[key] = robotMutation.removeLink(currChild)
                else:
                    newSynap = self.MutateSynapses(currChild[3])
                    currChild[3] = newSynap
                    self.children[key] = currChild

    def MutateSynapses(self, sypArr):
        mutateNum = numpy.random.randint(len(sypArr))
        sypArr[mutateNum][2] = random.random() * 2 - 1
        return sypArr

    def Select(self):
        for key in self.fitnessDictParents.keys():
            if self.fitnessDictParents[key] > self.fitnessDictChildren[key]:
                self.parents[key] = copy.deepcopy(self.children[key])
                self.fitnessDictParents[key] = self.fitnessDictChildren[key]
        for key in self.fitnessDictParents:
            self.fitnessPlotData[key][self.curGen] = self.fitnessDictParents[key]
        self.curGen = self.curGen + 1
        
    def Evaluate(self, solutions, isParent):
        for bot in solutions:
            runSim.Start_Simulation(solutions[bot], "DIRECT")
        if isParent:
            for bot in solutions:
                currFitness = runSim.Wait_For_Simulation_To_End(solutions[bot][4])
                self.fitnessDictParents[solutions[bot][4]] = currFitness
        else:
            for bot in solutions:
                currFitness = runSim.Wait_For_Simulation_To_End(solutions[bot][4])
                self.fitnessDictChildren[bot] = currFitness

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, False)
        self.Print()
        self.Select()

    def Print(self):
        print("")
        print("")
        for key in self.fitnessDictParents:
            print("Parent " + str(key) + ": " + str(self.fitnessDictParents[key]) + " Child: " + str(self.fitnessDictChildren[key]))
        print("")