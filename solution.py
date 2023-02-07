import pyrosim.pyrosim as pyrosim
import os
import numpy
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = nextID
        pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        for i in range(c.stairs):
            boxLoc = i
            # back stairs
            pyrosim.Send_Cube(name="Box", pos=[-3 - (boxLoc * 2),0,0.33 + (boxLoc / 3)] , size=[2,10,0.33 + (boxLoc / 3)], mass = 100)
            # front stairs
            pyrosim.Send_Cube(name="Box", pos=[3 + (boxLoc * 2),0,0.33 + (boxLoc / 3)] , size=[2,10,0.33 + (boxLoc / 3)], mass = 100)
        pyrosim.End()
    pass

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1.5,3,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1],jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,0,0] , size=[0.5,3,0.3])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-1,0,1],jointAxis = "0 1 0")    
        pyrosim.Send_Cube(name="LeftLeg", pos=[0,0,0] , size=[0.5,3,0.3])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.35,-0.7,0],jointAxis = "0 1 0")    
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0.75,-0.5] , size=[0.6,3,1])
        pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-0.35,0.7,0],jointAxis = "0 1 0")    
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,-0.75,-0.5] , size=[0.6,3,1])
        pyrosim.End()
        #exit()
        pass

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 2 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "LeftLeg_LeftLowerLeg")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn + 2 , weight = self.Send_Synapse(currentRow, currentColumn))
        pyrosim.End()

    def Mutate(self):
        self.weights[random.randint(0, c.numSensorNeurons - 1)][random.randint(0, c.numMotorNeurons - 1)] = random.random() * 2 - 1

    
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
        #self.Create_World()
        #self.Create_Body()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    def Set_ID(self, id):
        self.myID = id

    def Send_Synapse(self, currentRow, currentColumn):
        return self.weights[currentRow][currentColumn]