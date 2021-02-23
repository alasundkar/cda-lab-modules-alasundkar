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

	
	def __init__(self,  sensorType: int = ConfigConst.DEFAULT_SENSOR_TYPE, sensorName = ConfigConst.NOT_SET, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):
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
		self.senseData = SensorData( self.sensorType)
		if self.useRandomizer:
			self.senseData.setValue(random.randint(self.DEFAULT_MIN_VAL, self.DEFAULT_MAX_VAL))
		else:
			self.senseData.setValue(random.randint(self.DEFAULT_MIN_VAL, self.DEFAULT_MAX_VAL))
			if self.currentDataSetIndex >= 0 :
			#	sd.setValue(self.dataSet.dataEntries[self.currentDataSetIndex])
			
			#else:
			#	self.currentDataSetIndex = 0
				self.dataSetIndex = self.dataSetIndex + 1
			else:
				self.dataSetIndex = 0
		return self.senseData
	
	#			sd.setValue(self.dataSet[self.currentDataSetIndex])
	#	self.currentDataSetIndex += 1
	#	self.latestSensorData = sd
	#	return self.latestSensorData
	
	def getTelemetryValue(self) -> float:
		"""
		returns the sensor value
		"""
		self.senseData = None
		if self.latestSensorData is None:
			self.senseData = self.generateTelemetry()
		else:
			self.senseData = self.latestSensorData
		return self.senseData.getValue()
	