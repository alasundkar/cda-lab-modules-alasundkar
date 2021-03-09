#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from json import JSONEncoder
import json
import logging
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataUtil():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, encodeToUtf8 = False):
		pass
	
	def actuatorDataToJson(self, actuatorData):
		pass
	
	def sensorDataToJson(self, sensorData):
		pass

	def systemPerformanceDataToJson(self, sysPerfData):
		pass
	
	def jsonToActuatorData(self, jsonData):
		pass
	
	def jsonToSensorData(self, jsonData):
		pass
	
	def jsonToSystemPerformanceData(self, jsonData):
		pass
	
class JsonDataEncoder(JSONEncoder):
	"""
	Convenience class to facilitate JSON encoding of an object that
	can be converted to a dict.
	
	"""
	def default(self, o):
		return o.__dict__
	