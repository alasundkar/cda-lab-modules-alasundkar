#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#
import logging
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.SensorData import SensorData

class BaseSystemUtilTask():
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, name, typeID, sensorName = ConfigConst.NOT_SET):
		###
		# TODO: fill in the details here
		self.latestSensorData = None
		self.name=name
		self.typeID=typeID
		
		#pass
	
	def generateTelemetry(self) -> SensorData:
		###
		# TODO: fill in the details here
		#
		# NOTE: Use self._getSystemUtil() to retrieve the value from the sub-class
		pass
		
	def getTelemetryValue(self) -> float:
		#pass
		"""
		returns and logs Telemetry value from derived class _getSystemUtil .
		
		"""
		val = self._getSystemUtil()
		logging.info("Sub class name: %s Value of Telemetry is %s.", self.__class__.__name__, str(val))
		return val
	
	def _getSystemUtil(self) -> float:
		"""
		Template method implemented by sub-class.
		
		Retrieve the system utilization value as a float.
		
		@return float
		"""
		pass
		