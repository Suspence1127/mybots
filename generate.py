import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
dimensions = 1
for x in range(10):
    for y in range(5):
        for z in range(5):
            pyrosim.Send_Cube(name="Box", pos=[y,z,0.5 + x] , size=[dimensions,dimensions,dimensions])
    dimensions = dimensions * 0.9
pyrosim.End()