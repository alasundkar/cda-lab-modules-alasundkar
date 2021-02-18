#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.BaseIotData import BaseIotData

class SensorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 10.0
	DEFAULT_SENSOR_TYPE = 0
		
	def __init__(self, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		super(SensorData, self).__init__(name = name, typeID = typeID, d = d)
		self.value = ConfigConst.DEFAULT_VAL

		if d:
			self.sensorType = d['sensorType']
			self.value = d['value']
			self.name = d['name']
		else:
			self.sensorType = typeID
			self.value = self.DEFAULT_VAL
			self.name = name
	
	def getSensorType(self) -> int:
		"""
		Returns the sensor type to the caller.
		
		@return int
		"""
		return self.sensorType
	
	def getValue(self) -> float:
		"""
		Returns the sensor data 
		"""
		return self.value
	
	def setValue(self, newVal: float):
		'''
		Updates the new SensorData value.
		@param newVal: new Sensor data 
		'''
		self.updateTimeStamp()
		self.value = newVal

		
	def _handleUpdateData(self, data):
		'''
		Calls method to update the new 'data' received.
		@param data: updated Sensor data
		'''
		if data and isinstance(data, SensorData):
			self.setValue(data.getValue())
