#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import random

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataSet

class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	DEFAULT_MIN_VAL = ConfigConst.DEFAULT_VAL
	DEFAULT_MAX_VAL = 1000.0
	currentDataSetIndex = 0

	
	def __init__(self, sensorName = ConfigConst.NOT_SET, sensorType: int = ConfigConst.DEFAULT_SENSOR_TYPE, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):
		self.sensorType = sensorType
		self.dataSet = dataSet
		#self.minVal = minVal
		#self.maxVal = maxVal
		self.senseData = None
		self.sensorName = sensorName
		  
		self.useRandomizer = False    
		self.latestSensorData = None
		"""
		Created an index to store current DataSet index
		"""
		self.dataSetIndex = 0
		
		if dataSet == None:
			self.useRandomizer = True
			self.minVal = minVal	
			self.maxVal = maxVal
	def generateTelemetry(self) -> SensorData:
		"""
		generates sensor data and returns it
		"""
		sd = SensorData()
		sd.DEFAULT_SENSOR_TYPE = self.sensorType
		if self.useRandomizer:
			sd.setValue(random.randint(self.DEFAULT_MIN_VAL, self.DEFAULT_MAX_VAL))
		else:
			if self.currentDataSetIndex >= 0 and self.currentDataSetIndex < len(self.dataSet.dataEntries):
				sd.setValue(self.dataSet.dataEntries[self.currentDataSetIndex])
			else:
				self.currentDataSetIndex = 0
				sd.setValue(self.dataSet[self.currentDataSetIndex])
		self.currentDataSetIndex += 1
		self.latestSensorData = sd
		return self.latestSensorData
	
	def getTelemetryValue(self) -> float:
		"""
		returns the sensor value
		"""
		sd = None
		if self.latestSensorData is None:
			sd = self.generateTelemetry()
		else:
			sd = self.latestSensorData
		return sd.getValue()
	