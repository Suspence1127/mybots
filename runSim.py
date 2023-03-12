import pyrosim.pyrosim as pyrosim
import os
import numpy
import random
import time
import constants as c
import link
import joint

# Creates empty world for the snake
def Create_World(self):
    pyrosim.Start_SDF("world.sdf")
    pyrosim.End()
    pass

# Creates the body of the robot based on the map
def Create_Body(linkDict, jointDict, linkSensor, id):
    pyrosim.Start_URDF("body" + str(id) + ".urdf")
        # creates first link
    link0 = linkDict["Link0"]
    if "Link0" in linkSensor:
        pyrosim.Send_Cube(name=link0.name, pos=link0.position , size=[link0.x, link0.y, link0.z], colorString='"0 1.0 0 1.0"', colorName='"Green"')
    else:
        pyrosim.Send_Cube(name=link0.name, pos=link0.position , size=[link0.x, link0.y, link0.z], colorString='"0 0 1.0 1.0"', colorName='"Blue"')
    addBack0 = linkDict.pop("Link0")
    # Creates the rest of the links
    for link in linkDict.values():
        if link.name in linkSensor:
            pyrosim.Send_Cube(name=link.name, pos=link.position , size=[link.x, link.y, link.z], colorString='"0 1.0 0 1.0"', colorName='"Green"')
        else:
            pyrosim.Send_Cube(name=link.name, pos=link.position , size=[link.x, link.y, link.z], colorString='"0 0 1.0 1.0"', colorName='"Blue"')
        # Creates the joints
    for joint in jointDict.values():
        pyrosim.Send_Joint( name = joint.name , parent= joint.parent, child = joint.child , type = "revolute", position = joint.position,jointAxis = joint.axis)
    pyrosim.End()
    linkDict["Link0"] = addBack0
    pass

def Create_Brain(jointDict, linkSensor, synapseDict, id, numberLinks):
    pyrosim.Start_NeuralNetwork("brain" + str(id) + ".nndf")
    motorWeightCount = 0
    for joint in jointDict.values():
        pyrosim.Send_Motor_Neuron(name = motorWeightCount, jointName=joint.name)
        motorWeightCount = motorWeightCount + 1
    sensorCount = motorWeightCount
    for linkNum in range(numberLinks):
        if "Link" + str(linkNum) in linkSensor:
            pyrosim.Send_Sensor_Neuron(name = sensorCount, linkName="Link" + str(linkNum))
            sensorCount = sensorCount + 1
    for syp in synapseDict.values():
            pyrosim.Send_Synapse( sourceNeuronName = syp[0], targetNeuronName = syp[1], weight = syp[2])
    pyrosim.End()

def Evaluate(directOrGUI):
    Start_Simulation()
    Wait_For_Simulation_To_End(directOrGUI)

def Wait_For_Simulation_To_End(id):
    # while not os.path.exists("fitness" + str(id) + ".txt"):
    #     time.sleep(0.01)
    opened = False
    while not opened:
        try:
            f = open("fitness" + str(id) + ".txt", "r")
            opened = True
        except:
            continue
    fitness = float(f.read())
    f.close()
    os.system("del fitness" + str(id) + ".txt")
    return fitness

def Start_Simulation(robot, directOrGUI):
    # Robot = [self.linkDict, self.jointDict, self.linkSensor, self.synapseDict, self.myID, self.numLinks]
    # Determines the number of links for the snake
    #Create_World()
    Create_Brain(robot[1], robot[2], robot[3], robot[4], robot[5])
    Create_Body(robot[0], robot[1], robot[2], robot[4])
    # see pyrosim errors
    #os.system("start /B python3 simulate.py " + directOrGUI + " " + str(robot[4]))
    # dont see pyrosim errors
    os.system("start /B python3 -W ignore simulate.py " + directOrGUI + " " + str(robot[4]) + " >NUL 2>&1")
