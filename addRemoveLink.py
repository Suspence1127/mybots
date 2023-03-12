import pyrosim.pyrosim as pyrosim
import os
import numpy
import random
import time
import constants as c
import link
import joint

class robotMutation:
    # Calculates the absolute center of the link
    def centerCalculator(prevCenter, x1, y1, z1, face, x2, y2, z2):
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
            return [prevCenter[0], prevCenter[1], prevCenter[2] - (z1 / 2) - (z2 / 2)]
    
    # Checks if a potential new link overlaps any of the existing links
    def noOverlap(newCenter, xf, yf, zf, linkDict):
        for link in linkDict.values():
            linkMin = [link.center[0] - link.x/2, link.center[1] - link.y/2, link.center[2] - link.z/2]
            linkMax = [link.center[0] + link.x/2, link.center[1] + link.y/2, link.center[2] + link.z/2]
            newLinkMin = [newCenter[0] - xf/2, newCenter[1] - yf/2, newCenter[2] - zf/2]
            newLinkMax = [newCenter[0] + xf/2, newCenter[1] + yf/2, newCenter[2] + zf/2]
            # Check if the new link overlaps with any of the existing links in linkDict or if its below the floor
            if (newLinkMin[0] <= linkMax[0] and newLinkMax[0] >= linkMin[0] and
                newLinkMin[1] <= linkMax[1] and newLinkMax[1] >= linkMin[1] and
                newLinkMin[2] <= linkMax[2] and newLinkMax[2] >= linkMin[2]) or newLinkMin[2] < 0.1:
                return False 
        return True
    
    # Returns the face on the current link that is connected to the previous link
    def faceConnect(face):
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

    # Adds elements to the joint dictionary    
    def addJoint(name1, x1, y1, z1, name2, face, parentJointFace, jointDict):
        #axisIndex = numpy.random.randint(6)
        #axisArray = ["1 0 0", "-1 0 0", "0 1 0", "0 -1 0", "0 0 1", "0, 0, -1"]
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
            jointDict["Link0_" + name2] = joint.JOINT("Link0_" + name2, position, "Link0", name2, axis, face)
        else:
            prevJointFace = robotMutation.faceConnect(parentJointFace.face)
            if face == 0:
                if prevJointFace == 0:
                    return "error"
                elif prevJointFace == 1:
                    position = [x1, 0, 0]
                elif prevJointFace == 2:
                    position = [x1 / 2, -y1 / 2, 0]
                elif prevJointFace == 3:
                    position = [x1 / 2, y1 / 2, 0]
                elif prevJointFace == 4:
                    position = [x1 / 2, 0, -z1 / 2]
                else:
                    position = [x1 / 2, 0, z1 / 2]
                axis = "0 1 0"
            elif face == 1:
                if prevJointFace == 0:
                    position = [-x1, 0, 0]
                elif prevJointFace == 1:
                    return "error"
                elif prevJointFace == 2:
                    position = [-x1 / 2, -y1 / 2, 0]
                elif prevJointFace == 3:
                    position = [-x1 / 2, y1 / 2, 0]
                elif prevJointFace == 4:
                    position = [-x1 / 2, 0, -z1 / 2]
                else:
                    position = [-x1 / 2, 0, z1 / 2]
                axis = "0 1 0"
            elif face == 2:
                if prevJointFace == 0:
                    position = [-x1 / 2, y1 / 2, 0]
                elif prevJointFace == 1:
                    position = [x1 / 2, y1 / 2, 0]
                elif prevJointFace == 2:
                    return "error"
                elif prevJointFace == 3:
                    position = [0, y1, 0]
                elif prevJointFace == 4:
                    position = [0, y1 / 2, -z1 / 2]
                else:
                    position = [0, y1 / 2, z1 / 2]
                axis = "0 1 0"
            elif face == 3:
                if prevJointFace == 0:
                    position = [-x1 / 2, -y1 / 2, 0]
                elif prevJointFace == 1:
                    position = [x1 / 2, -y1 / 2, 0]
                elif prevJointFace == 2:
                    position = [0, -y1, 0]
                elif prevJointFace == 3:
                    return "error"
                elif prevJointFace == 4:
                    position = [0, -y1 / 2, -z1 / 2]
                else:
                    position = [0, -y1 / 2, z1 / 2]
                axis = "0 1 0"
            elif face == 4:
                if prevJointFace == 0:
                    position = [-x1 / 2, 0, z1 / 2] 
                elif prevJointFace == 1:
                    position = [x1 / 2, 0, z1 / 2]
                elif prevJointFace == 2:
                    position = [0, -y1 / 2, z1 / 2]
                elif prevJointFace == 3:
                    position = [0, y1 / 2, z1 / 2]
                elif prevJointFace == 4:
                    return "error"
                else:
                    position = [0, 0, z1]
                axis = "0 0 1"
            else:
                if prevJointFace == 0:
                    position = [-x1 / 2, 0, -z1 / 2] 
                elif prevJointFace == 1:
                    position = [x1 / 2, 0, -z1 / 2]
                elif prevJointFace == 2:
                    position = [0, -y1 / 2, -z1 / 2]
                elif prevJointFace == 3:
                    position = [0, y1 / 2, -z1 / 2]
                elif prevJointFace == 4:
                    position = [0, 0, -z1]
                else:
                    return "error"
                axis = "0 0 1"
            jointDict[name1 + "_" + name2] = joint.JOINT(name1 + "_" + name2, position, name1, name2, axis, face)
        return jointDict

    # Finds the link position relative to the joint depending on the face
    def findLinkPos(parentFace, x, y, z):
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

    # Finds the parent joint in order to later calculate relative position    
    def findParentJoint(parentLink, jointDict):
        for link in jointDict.keys():
            if "_" + parentLink in link:
                #print(self.jointDict[link])
                return jointDict[link]
        return None
    
    def checkEndLink(currLink, jointDict):
        for link in jointDict.keys():
            if currLink + "_" in link:
                return False
        return True
    
    def removeLink(robot):
        # Robot = [self.linkDict, self.jointDict, self.linkSensor, self.synapseDict, self.myID, self.numLinks, self.actualNumLinks]
        linkDict = robot[0]
        foundLink = False
        while not foundLink:
            currLink = numpy.random.randint(len(linkDict))
            foundLink = robotMutation.checkEndLink(linkDict["Link" + str(currLink)].name, robot[1])
        removedLink = linkDict["Link" + str(currLink)]
        removedLink.faces = [1, 1, 1, 1, 1, 1]
        removedLink.x = 0
        removedLink.y = 0
        removedLink.z = 0
        linkDict["Link" + str(currLink)] = removedLink
        robot[0] = linkDict
        robot[6] = robot[6] - 1
        return robot

    def addSynapses(linkSensor, synapseDict):
        linkNum = synapseDict[0][0]
        sensorNames = set()
        for key in synapseDict.keys():
            synapseDict[key] = [synapseDict[key][0] + 1, synapseDict[key][1], synapseDict[key][2]]
            sensorNames.add(synapseDict[key][0])
            newKey = key + 1
        for element in sensorNames:
            synapseDict[newKey] = [element, linkNum, random.random() * 2 - 1]
            newKey = newKey + 1
        return synapseDict

    def addLink(robot):
        # Robot = [self.linkDict, self.jointDict, self.linkSensor, self.synapseDict, self.myID, self.numLinks, self.actualNumLinks]
        numberLinks = robot[5]
        actualNumLinks = robot[6]
        linkDict = robot[0]
        jointDict = robot[1]
        synapseDict = robot[3]
        currLinkName = numberLinks
        while currLinkName < numberLinks + 1:
            parentLink = linkDict["Link" + str(numpy.random.randint(0, len(linkDict)))]
            if 0 in parentLink.faces:
                empty = False
                while empty == False:
                    face = numpy.random.randint(0, 6)
                    if parentLink.faces[face] == 0:
                        empty = True
                randNums = numpy.random.rand(3,1) * 1.5 + 0.5
                #randNums = [[1],[1],[1]]
                newCenter = robotMutation.centerCalculator(parentLink.center, parentLink.x, parentLink.y, parentLink.z, face, randNums[0][0], randNums[1][0], randNums[2][0])
                if robotMutation.noOverlap(newCenter, randNums[0][0], randNums[1][0], randNums[2][0], linkDict):
                    #print("parent: " + parentLink.name + " child: " + str(currLinkName))
                    parentLink.faces[face] = 1
                    linkDict[parentLink.name] = parentLink
                    newFaces = [0, 0, 0, 0, 0, 0]
                    newFaces[robotMutation.faceConnect(face)] = 1
                    linkDict["Link" + str(currLinkName)] = link.LINK("Link" + str(currLinkName), newCenter, robotMutation.findLinkPos(face, randNums[0][0], randNums[1][0], randNums[2][0]), randNums[0][0], randNums[1][0], randNums[2][0], newFaces, [parentLink.name, face, robotMutation.faceConnect(face)])
                    parentJointFace = robotMutation.findParentJoint(parentLink.name, jointDict)
                    jointDict = robotMutation.addJoint(parentLink.name, parentLink.x, parentLink.y, parentLink.z, "Link" + str(currLinkName), face, parentJointFace, jointDict)
                    currLinkName = currLinkName + 1
                    if len(synapseDict) > 0:
                        synapseDict = robotMutation.addSynapses(robot[2], synapseDict)
        return [linkDict, jointDict, robot[2], synapseDict, robot[4], numberLinks + 1, actualNumLinks + 1]