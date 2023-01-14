import numpy
import matplotlib.pyplot as pyplot
backLegSensorValues = numpy.load('data/outputBack.npy')
frontLegSensorValues = numpy.load('data/outputFront.npy')
pyplot.plot(backLegSensorValues, label='Back', linewidth=4)
pyplot.plot(frontLegSensorValues, label='Front')
pyplot.legend()
pyplot.show()