import os
import hillclimber

# for i in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

hc = hillclimber.HILL_CLIMBER()
hc.Evolve()