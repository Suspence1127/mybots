from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT()
        pass

    def Run(self):
        for x in range(c.iterations):
            time.sleep(c.sleepTime)
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x)
        #numpy.save('data/outputBack.npy', backLegSensorValues)
        #numpy.save('data/outputFront.npy', frontLegSensorValues)
        pass

    def __del__(self):
        p.disconnect()
        pass