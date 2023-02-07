import solution
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = dict()
        self.nextAvailableID = 0
        for num in range(c.populationSize):
            self.parents[num] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")
        self.Show_Best()
        pass

    def Show_Best(self):
        bestKey = 0
        for key in self.parents:
            if self.parents[key].fitness > self.parents[bestKey].fitness:
                bestKey = key
        self.parents[bestKey].Start_Simulation("GUI")
        print(self.parents[bestKey].fitness)
        pass

    def Spawn(self):
        self.children = dict()
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness < self.children[key].fitness:
                self.parents[key] = self.children[key]
        
    def Evaluate(self, solutions):
        for bot in solutions:
            solutions[bot].Start_Simulation("DIRECT")
        for bot in solutions:
            solutions[bot].Wait_For_Simulation_To_End("DIRECT")

    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Print(self):
        print("")
        print("")
        for key in self.parents:
            print("Parent " + str(key) + ": " + str(self.parents[key].fitness) + " Child: " + str(self.children[key].fitness))
        print("")