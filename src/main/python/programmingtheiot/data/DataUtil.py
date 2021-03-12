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
		if not actuatorData:
			logging.warning("ActuatorData is null. Ignoring conversion to JSON.")
			return None
		logging.debug("Encoding ActuatorData to JSON [pre]  --> " + str(actuatorData))
		jsonData = json.dumps(actuatorData, indent = 4, cls = JsonDataEncoder)
		logging.debug("Encoding ActuatorData to JSON [post] --> " + str(jsonData))
		return jsonData
	
	def sensorDataToJson(self, sensorData):
		if not sensorData:
			logging.warning("sensorData is null. Ignoring conversion to JSON.")
			return None
		logging.debug("Encoding sensorData to JSON [pre]  --> " + str(sensorData))
		jsonData = json.dumps(sensorData, indent = 4, cls = JsonDataEncoder)
		logging.debug("Encoding sensorData to JSON [post] --> " + str(jsonData))
		return jsonData

	def systemPerformanceDataToJson(self, sysPerfData):
		if not sysPerfData:
			logging.warning("sysPerfData is null. Ignoring conversion to JSON.")
			return None
		logging.debug("Encoding sysPerfData to JSON [pre]  --> " + str(sysPerfData))
		jsonData = json.dumps(sysPerfData, indent = 4, cls = JsonDataEncoder)
		logging.debug("Encoding sysPerfData to JSON [post] --> " + str(jsonData))
		return jsonData
	
	def jsonToActuatorData(self, jsonData):
		if not jsonData:
			logging.warning("JSON data is empty or null.")
			return None
		jsonData = jsonData.replace("\'", "\"").replace('False', 'false').replace('True', 'true')
		ad = ActuatorData()
		jsonStruct = json.loads(jsonData)
		self._updateIotData(jsonStruct, ad)
		return ad
	
	def jsonToSensorData(self, jsonData):
		if not jsonData:
			logging.warning("JSON data is empty or null.")
			return None
		jsonData = jsonData.replace("\'", "\"").replace('False', 'false').replace('True', 'true')
		ad = SensorData()
		jsonStruct = json.loads(jsonData)
		self._updateIotData(jsonStruct, ad)
		return ad
	
	def jsonToSystemPerformanceData(self, jsonData):
		if not jsonData:
			logging.warning("JSON data is empty or null.")
			return None
		jsonData = jsonData.replace("\'", "\"").replace('False', 'false').replace('True', 'true')
		ad = SystemPerformanceData()
		jsonStruct = json.loads(jsonData)
		self._updateIotData(jsonStruct, ad)
		return ad
	
	def _formatDataAndLoadDictionary(self, jsonData: str) -> dict:
		jsonData = jsonData.replace("\'", "\"").replace( 'False', 'false').replace('True', 'true')
		jsonStruct = json.loads(jsonData)
		return jsonStruct
	
	def _updateIotData(self, jsonStruct, obj):
		varStruct = vars(obj)
		for key in jsonStruct:
			if key in varStruct:
				setattr(obj, key, jsonStruct[key])
			else:
				logging.warn("JSON data key not mappable to object: %s", key)

class JsonDataEncoder(JSONEncoder):
	"""
	Convenience class to facilitate JSON encoding of an object that
	can be converted to a dict.
	
	"""
	def default(self, o):
		return o.__dict__
	