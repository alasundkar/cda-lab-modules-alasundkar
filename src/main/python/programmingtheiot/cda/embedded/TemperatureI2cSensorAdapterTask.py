#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#


import logging
#import smbus
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask

class TemperatureI2cSensorAdapterTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		super(TemperatureI2cSensorAdapterTask, self).__init__(SensorData.TEMP_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP, maxVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)

	
	def generateTelemetry(self) -> SensorData:
		pass
	
	def getTelemetryValue(self) -> float:
		pass
	