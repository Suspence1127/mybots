import time
import pybullet as p
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for x in range(1000):
    print(x)
    time.sleep(1/60)
    p.stepSimulation()
p.disconnect()