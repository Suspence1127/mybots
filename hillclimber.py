import solution
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = solution.SOLUTION()
        pass

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation("DIRECT")
        self.Show_Best()

    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        pass

    def Mutate(self):
        self.child.Mutate()
        pass

    def Select(self):
        print("")
        print("")
        print("Parent: " + str(self.parent.fitness) + " - Child: " + str(self.child.fitness))
        print("")
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child
        pass

    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(directOrGUI)
        self.Select()