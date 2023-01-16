import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import random
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf", [0, 0, 0.5])
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
frequency = 25
phaseOffset = numpy.pi/4
amplitude = numpy.pi/4
targetAngles = amplitude * numpy.sin(frequency * numpy.linspace(-numpy.pi/4, numpy.pi/4, 1000) + phaseOffset)
targetAngles2 = amplitude * numpy.sin(frequency * numpy.linspace(-numpy.pi/4, numpy.pi/4, 1000) + 0)
pyrosim.Prepare_To_Simulate(robotId)
for x in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition =targetAngles[x],maxForce = 150)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition =targetAngles2[x],maxForce = 150)
numpy.save('data/outputBack.npy', backLegSensorValues)
numpy.save('data/outputFront.npy', frontLegSensorValues)
p.disconnect()