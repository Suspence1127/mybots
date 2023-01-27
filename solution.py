import pyrosim.pyrosim as pyrosim
import os
import numpy
import random

class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(3, 2) * 2 - 1
        pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] , size=[1,1,1])
        pyrosim.End()
    pass

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [-0.5,0,1])    
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.End()
        pass

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        linkNames = [0, 1, 2]
        motorNames = [0, 1]
        for currentRow in linkNames:
            for currentColumn in motorNames:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.Send_Synapse(currentRow, currentColumn))
        pyrosim.End()

    def Mutate(self):
        self.weights[random.randint(0, 2)][random.randint(0,1)] = random.random() * 2 - 1

    
    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI)
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()
        pass

    def Send_Synapse(self, currentRow, currentColumn):
        return self.weights[currentRow][currentColumn]