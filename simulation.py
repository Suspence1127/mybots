import time
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
pyrosim.Prepare_To_Simulate(robotId)
for x in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
numpy.save('data/outputBack.npy', backLegSensorValues)
numpy.save('data/outputFront.npy', frontLegSensorValues)
p.disconnect()