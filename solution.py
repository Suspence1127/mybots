import pyrosim.pyrosim as pyrosim
import os
import numpy
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextID):
        self.weights = 0
        self.linkSensor = set()
        self.myID = nextID
        pass

    # Creates empty world for the snake
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
    pass

    # Creates the randomized body for the snake
    def Create_Body(self, numberLinks):
        pyrosim.Start_URDF("body.urdf")
        # link can be any dimensions between 0.5 and 2
        randNums = numpy.random.rand(3,1) * 1.5 + 0.5
        # creates first link
        if "Link0" in self.linkSensor:
            pyrosim.Send_Cube(name="Link0", pos=[0,0,2] , size=[randNums[0][0],randNums[1][0],randNums[2][0]], colorString='"0 1.0 0 1.0"', colorName='"Green"')
        else:
            pyrosim.Send_Cube(name="Link0", pos=[0,0,2] , size=[randNums[0][0],randNums[1][0],randNums[2][0]], colorString='"0 0 1.0 1.0"', colorName='"Blue"')
        # creates first joint
        pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1", type = "revolute", position = [randNums[0][0] / 2,0,2],jointAxis = "0 1 0")

        # Creates the rest of the links
        for linkNum in range(1, numberLinks):
            randNums = numpy.random.rand(3,1) * 2 + 0.5
            if "Link" + str(linkNum) in self.linkSensor:
                pyrosim.Send_Cube(name="Link" + str(linkNum), pos=[randNums[0][0] / 2,0,0] , size=[randNums[0][0],randNums[1][0],randNums[2][0]], colorString='"0 1.0 0 1.0"', colorName='"Green"')
            else:
                pyrosim.Send_Cube(name="Link" + str(linkNum), pos=[randNums[0][0] / 2,0,0] , size=[randNums[0][0],randNums[1][0],randNums[2][0]], colorString='"0 0 1.0 1.0"', colorName='"Blue"')
            if linkNum < numberLinks - 1:
                pyrosim.Send_Joint( name = "Link" + str(linkNum) + "_Link" + str(linkNum + 1) , parent= "Link" + str(linkNum) , child = "Link" + str(linkNum + 1) , type = "revolute", position = [randNums[0][0],0,0],jointAxis = "0 1 0")
        pyrosim.End()
        pass

    def Create_Brain(self, numberLinks):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        motorWeightCount = 0
        for linkNum in range(numberLinks - 1):
            motorWeightCount = motorWeightCount + 1
            pyrosim.Send_Motor_Neuron(name = linkNum, jointName="Link" + str(linkNum) + "_Link" + str(linkNum + 1))
        sensorCount = numberLinks - 1
        sensWeightCount = 0
        for linkNum in range(numberLinks):
            sensorExists = numpy.random.randint(2)
            if sensorExists == 0:
                sensWeightCount = sensWeightCount + 1
                pyrosim.Send_Sensor_Neuron(name = sensorCount, linkName="Link" + str(linkNum))
                self.linkSensor.add("Link" + str(linkNum))
                sensorCount = sensorCount + 1
        self.weights = numpy.random.rand(sensWeightCount, motorWeightCount) * 2 - 1
        self.numSensorNeurons = sensWeightCount
        self.numMotorNeurons = motorWeightCount
        for currentRow in range(sensWeightCount):
            for currentColumn in range(numberLinks - 1):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow + numberLinks - 1, targetNeuronName = currentColumn, weight = self.Send_Synapse(currentRow, currentColumn))
        pyrosim.End()

    def Mutate(self):
        self.weights[random.randint(0, self.numSensorNeurons - 1)][random.randint(0, self.numMotorNeurons - 1)] = random.random() * 2 - 1

    
    def Evaluate(self, directOrGUI):
        self.Start_Simulation()
        self.Wait_For_Simulation_To_End(directOrGUI)

    def Wait_For_Simulation_To_End(self, directOrGUI):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")


    def Start_Simulation(self, directOrGUI):
        # Determines the number of links for the snake
        numLinks = numpy.random.randint(3,15)
        self.Create_World()
        self.Create_Brain(numLinks)
        self.Create_Body(numLinks)
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    def Set_ID(self, id):
        self.myID = id

    def Send_Synapse(self, currentRow, currentColumn):
        return self.weights[currentRow][currentColumn]