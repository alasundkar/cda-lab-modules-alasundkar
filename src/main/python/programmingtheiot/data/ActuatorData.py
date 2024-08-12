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
import logging

class ActuatorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
# 	DEFAULT_COMMAND = 0
# 	#COMMAND_OFF = DEFAULT_COMMAND
# 	COMMAND_OFF = 0
#	COMMAND_ON = 1
# 	command = ConfigConst.DEFAULT_COMMAND
#	DEFAULT_COMMAND = COMMAND_ON
# 	DEFAULT_VAL = 0.0
	##value = ConfigConst.DEFAULT_VAL

	# for now, actuators will be 1..99
	# and displays will be 100..1999

	DEFAULT_ACTUATOR_TYPE = 0
	
	HVAC_ACTUATOR_TYPE = 1
	HUMIDIFIER_ACTUATOR_TYPE = 2
	LED_DISPLAY_ACTUATOR_TYPE = 100
	DEFAULT_STATE_DATA = "{state: None}"
	actuatorType = None
#	DEFAULT_ACTUATOR_TYPE = 0

	def __init__(self, typeID: int = ConfigConst.DEFAULT_ACTUATOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		super(ActuatorData, self).__init__(name = name, typeID = typeID, d = d)
		self.command = ConfigConst.DEFAULT_COMMAND
		self.stateData = None
		self.value = ConfigConst.DEFAULT_VAL
	
	def getCommand(self) -> int:
		return self.command
	
	def getStateData(self) -> str:
		return self.stateData

	def getValue(self) -> float:
		"""
		Returns float value of the actuator readings.
		"""
		return self.value
	
	def isResponseFlagEnabled(self) -> bool:
		return False
	
	def setCommand(self, command: int):
		self.command = command
	
	def setAsResponse(self):
		pass
		
	def setStateData(self, stateData: str):
		self.stateData = stateData

	def setValue(self, val: float):
		"""
		Modifies the default value readings of the actuator.
		"""
		self.updateTimeStamp()
		self.value = val
		print("print setvalue")
		print(self.value)
		
	def _handleUpdateData(self, data):
		"""
		Handles updated data.
		"""
		if data and isinstance(data, ActuatorData):    
			self.value = data.getValue()    
			self.command = data.getCommand()    
			self.stateData = data.getStateData()
		