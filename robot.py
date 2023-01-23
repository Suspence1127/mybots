from motor import MOTOR
from sensor import SENSOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import constants as c

class ROBOT:
    def __init__(self):
        self.motor = dict()
        self.sensors = dict()
        self.robotId = p.loadURDF("body.urdf", [0, 0, 0.1])
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        pass

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        pass

    def Sense(self, x):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(x)
        pass

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motor[jointName] = MOTOR(jointName)
        pass

    def Act(self, x):
        for jointName in pyrosim.jointNamesToIndices:
            self.motor[jointName].Set_Value(self.robotId, x)
        pass
