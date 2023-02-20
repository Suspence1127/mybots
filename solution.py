import pyrosim.pyrosim as pyrosim
import os
import numpy
import random
import time
import constants as c
import link
import joint

class SOLUTION:
    def __init__(self, nextID):
        self.weights = 0
        self.linkSensor = set()
        self.linkDict = dict()
        self.jointDict = dict()
        self.myID = nextID
        self.created = False
        self.created2 = False
        pass

    # Creates empty world for the snake
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
    pass

    def centerCalculator(self, prevCenter, x1, y1, z1, face, x2, y2, z2):
        if face == 0:
            return [prevCenter[0] + (x1 / 2) + (x2 / 2), prevCenter[1], prevCenter[2]]
        elif face == 1:
            return [prevCenter[0] - (x1 / 2) - (x2 / 2), prevCenter[1], prevCenter[2]]
        elif face == 2:
            return [prevCenter[0], prevCenter[1]  + (y1 / 2) + (y2 / 2), prevCenter[2]]
        elif face == 3:
            return [prevCenter[0], prevCenter[1]  - (y1 / 2) - (y2 / 2), prevCenter[2]]
        elif face == 4:
            return [prevCenter[0], prevCenter[1], prevCenter[2] + (z1 / 2) + (z2 / 2)]
        else:
            return [prevCenter[0], prevCenter[1], prevCenter[2] + (z1 / 2) + (z2 / 2)]
        
    def noOverlap(self, newCenter, xf, yf, zf):
        for link in self.linkDict.values():
            link_min = (
                link.center[0] - link.x/2,
                link.center[1] - link.y/2,
                link.center[2] - link.z/2
            )
            link_max = (
                link.center[0] + link.x/2,
                link.center[1] + link.y/2,
                link.center[2] + link.z/2
            )
            new_link_min = (
                newCenter[0] - xf/2,
                newCenter[1] - yf/2,
                newCenter[2] - zf/2
            )
            new_link_max = (
                newCenter[0] + xf/2,
                newCenter[1] + yf/2,
                newCenter[2] + zf/2
            )
            # Check if the new link overlaps with any of the existing links in linkDict
            if (new_link_min[0] <= link_max[0] and new_link_max[0] >= link_min[0] and
                new_link_min[1] <= link_max[1] and new_link_max[1] >= link_min[1] and
                new_link_min[2] <= link_max[2] and new_link_max[2] >= link_min[2]):
                return False 
        return True
    
    def faceConnect(self, face):
        if face == 0:
            return 1
        elif face == 1:
            return 0
        elif face == 2:
            return 3
        elif face == 3:
            return 2
        elif face == 4:
            return 5
        else:
            return 4
        
    def addJoint(self, name1, x1, y1, z1, name2, face):
        if name1 == "Link0":
            if face == 0:
                position = [x1 / 2,0,2]
                axis = "0 1 0"
            elif face == 1:
                position = [-x1 / 2,0,2]
                axis = "0 1 0"
            elif face == 2:
                position = [0,y1 / 2,2]
                axis = "1 0 0"
            elif face == 3:
                position = [0,-y1 / 2,2]
                axis = "1 0 0"
            elif face == 4:
                position = [0,0,(z1 / 2) + 2]
                axis = "0 0 1"
            else:
                position = [0,0,(-z1 / 2) + 2]
                axis = "0 0 1"
            self.jointDict["Link0_" + name2] = joint.JOINT("Link0_" + name2, position, "Link0", name2, axis)
        else:
            if face == 0:
                position = [x1, 0, 0]
                axis = "0 1 0"
            elif face == 1:
                position = [-x1, 0, 0]
                axis = "0 1 0"
            elif face == 2:
                position = [0, y1, 0]
                axis = "0 1 0"
            elif face == 3:
                position = [0, -y1, 0]
                axis = "0 1 0"
            elif face == 4:
                position = [0, 0, z1]
                axis = "0 0 1"
            else:
                position = [0, 0, -z1]
                axis = "0 0 1"
            self.jointDict[name1 + "_" + name2] = joint.JOINT(name1 + "_" + name2, position, name1, name2, axis)
        pass

    def findLinkPos(self, parentFace, x, y, z):
        if parentFace == 0:
            return [x/2, 0, 0]
        elif parentFace == 1:
            return [-x/2, 0, 0]
        elif parentFace == 2:
            return [0, y/2, 0]
        elif parentFace == 3:
            return [0, -y/2, 0]
        elif parentFace == 4:
            return [0, 0, z/2]
        elif parentFace == 5:
            return [0, 0, -z/2]

    def mapRobot(self, numberLinks):
        randNums = numpy.random.rand(3,1) * 1.5 + 0.5
        self.linkDict["Link0"] = link.LINK("Link0", [0, 0, 2], [0, 0, 2], randNums[0][0],randNums[1][0],randNums[2][0], [0, 0, 0, 0, 0, 1], None)
        currLinkName = 1
        while currLinkName < numberLinks:
            parentLink = self.linkDict["Link" + str(numpy.random.randint(0, len(self.linkDict)))]
            if 0 in parentLink.faces:
                empty = False
                while empty == False:
                    face = numpy.random.randint(0, 6)
                    if parentLink.faces[face] == 0:
                        empty = True
            randNums = numpy.random.rand(3,1) * 1.5 + 0.5
            newCenter = self.centerCalculator(parentLink.center, parentLink.x, parentLink.y, parentLink.z, face, randNums[0][0], randNums[1][0], randNums[2][0])
            if self.noOverlap(newCenter, randNums[0][0], randNums[1][0], randNums[2][0]):
                print("parent: " + parentLink.name + " child: " + str(currLinkName))
                parentLink.faces[face] = 1
                self.linkDict[parentLink.name] = parentLink
                newFaces = [0, 0, 0, 0, 0, 0]
                newFaces[self.faceConnect(face)] = 1
                self.linkDict["Link" + str(currLinkName)] = link.LINK("Link" + str(currLinkName), newCenter, self.findLinkPos(face, randNums[0][0], randNums[1][0], randNums[2][0]), randNums[0][0], randNums[1][0], randNums[2][0], newFaces, [parentLink.name, face, self.faceConnect(face)])
                self.addJoint(parentLink.name, parentLink.x, parentLink.y, parentLink.z, "Link" + str(currLinkName), face)
                currLinkName = currLinkName + 1
        pass

    # Creates the randomized body for the snake
    def Create_Body(self):
        # for elements in self.linkDict.values():
        #     print(elements)
        # for elements in self.jointDict.values():
        #     print(elements)
        # exit()
        pyrosim.Start_URDF("body.urdf")
        # creates first link
        link0 = self.linkDict["Link0"]
        if "Link0" in self.linkSensor:
            pyrosim.Send_Cube(name=link0.name, pos=link0.position , size=[link0.x, link0.y, link0.z], colorString='"0 1.0 0 1.0"', colorName='"Green"')
        else:
            pyrosim.Send_Cube(name=link0.name, pos=link0.position , size=[link0.x, link0.y, link0.z], colorString='"0 0 1.0 1.0"', colorName='"Blue"')
        self.linkDict.pop("Link0")
        # Creates the rest of the links
        for link in self.linkDict.values():
            if link.name in self.linkSensor:
                pyrosim.Send_Cube(name=link.name, pos=link.position , size=[link.x, link.y, link.z], colorString='"0 1.0 0 1.0"', colorName='"Green"')
            else:
                pyrosim.Send_Cube(name=link.name, pos=link.position , size=[link.x, link.y, link.z], colorString='"0 0 1.0 1.0"', colorName='"Blue"')
        # Creates the joints
        for joint in self.jointDict.values():
            pyrosim.Send_Joint( name = joint.name , parent= joint.parent, child = joint.child , type = "revolute", position = joint.position,jointAxis = joint.axis)
        pyrosim.End()
        pass

    def Create_Brain(self, numberLinks):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        motorWeightCount = 0
        for joint in self.jointDict.values():
            pyrosim.Send_Motor_Neuron(name = motorWeightCount, jointName=joint.name)
            motorWeightCount = motorWeightCount + 1
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
        numLinks = numpy.random.randint(3,c.botSize)
        self.Create_World()
        if not self.created:
            self.mapRobot(numLinks)
            self.created = True
        self.Create_Brain(numLinks)
        if not self.created2:
            self.Create_Body()
            self.created2 = True
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    def Set_ID(self, id):
        self.myID = id

    def Send_Synapse(self, currentRow, currentColumn):
        return self.weights[currentRow][currentColumn]