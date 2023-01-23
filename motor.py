import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.frequency = c.frequency
        self.amplitude = c.amplitude
        self.offset = c.phaseOffset
        self.Prepare_To_Act()
        pass

    def Prepare_To_Act(self):
        if self.jointName == "Torso_BackLeg":
            self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi, c.iterations) + self.offset)
        else:
            self.motorValues = self.amplitude * numpy.sin(1/2 * self.frequency * numpy.linspace(0, 2 * numpy.pi, c.iterations))
        pass

    def Set_Value(self, robotId, x):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = self.jointName ,controlMode = p.POSITION_CONTROL,targetPosition =self.motorValues[x],maxForce = c.maxForce)
        pass