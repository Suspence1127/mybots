import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION
from world import WORLD

simulation = SIMULATION()
simulation.Run()

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf", [0, 0, 0.5])
# p.loadSDF("world.sdf")
# backLegSensorValues = numpy.zeros(c.iterations)
# frontLegSensorValues = numpy.zeros(c.iterations)
# targetAngles = c.amplitude * numpy.sin(c.frequency * numpy.linspace(-numpy.pi/4, numpy.pi/4, c.iterations) + c.phaseOffset)
# targetAngles2 = c.amplitude * numpy.sin(c.frequency * numpy.linspace(-numpy.pi/4, numpy.pi/4, c.iterations) + 0)
# # pyrosim.Prepare_To_Simulate(robotId)
# for x in range(c.iterations):
#     time.sleep(c.sleepTime)
#     simulation.physicsClient.stepSimulation()
#     # backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     # frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     # pyrosim.Set_Motor_For_Joint(bodyIndex = simulation.robotId,jointName = "Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition =targetAngles[x],maxForce = c.maxForce)
#     # pyrosim.Set_Motor_For_Joint(bodyIndex = simulation.robotId,jointName = "Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition =targetAngles2[x],maxForce = c.maxForce)
# # numpy.save('data/outputBack.npy', backLegSensorValues)
# # numpy.save('data/outputFront.npy', frontLegSensorValues)
# simulation.physicsClient.disconnect()