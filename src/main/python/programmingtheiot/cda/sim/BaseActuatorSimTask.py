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

from programmingtheiot.data.ActuatorData import ActuatorData

class BaseActuatorSimTask():
# 	typeID = None
# 	simpleName = None
# 	latestActuatorData = None
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self,  typeID: int = ConfigConst.DEFAULT_ACTUATOR_TYPE,name: str = ConfigConst.NOT_SET, simpleName: str = "Actuator"):
		self.typeID = typeID
		self.simpleName = simpleName
		self.lastKnownCommand = ConfigConst.DEFAULT_COMMAND
		self.latestActuatorData = ActuatorData()				

	"""
	Activates actuator with input value and return if its successfull
	"""

	def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
	#def _activateActuator(self, val: float) -> bool:
		msg = "\n*******"
		msg = msg + "\n* O N *"
		msg = msg + "\n*******"
		msg = msg + "\n" + self.simpleName + " VALUE -> " + str(val) + "\n======="
			
		logging.info("Simulating %s actuator ON: %s", self.simpleName, msg)
		
		return 0
			
	"""
	Deactivates actuator and return if its successfully
	
	"""
	def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
		msg = "\n*******"
		msg = msg + "\n* OFF *"
		msg = msg + "\n*******"
		
		logging.info("Simulating %s actuator OFF: %s", self.name, msg)
				
		return 0
		
	def getLatestActuatorResponse(self) -> ActuatorData:
		pass
	
	def getSimpleName(self) -> str:
		pass
	
	def updateActuator(self, data: ActuatorData) -> bool:
		"""
		NOTE: If 'data' is valid, the actuator-specific work can be delegated
		to self._handleActuation, provided the sub-class implements this
		template method.
		"""
	#	if data and self.typeID == data.getTypeID(self):
		if data:
			statusCode = ConfigConst.DEFAULT_STATUS
			
			# check if the new command is the same as the old - if so, ignore
			curCommand = data.getCommand()
			
			if curCommand is self.lastKnownCommand:
				logging.debug("New actuator command is a repeat of current state. Ignoring: %s", str(curCommand))
			else:
				if curCommand == ConfigConst.COMMAND_ON:
					logging.info("Activating actuator...")
					statusCode = self._activateActuator(val = data.getValue(), stateData = data.getStateData())
				elif curCommand == ConfigConst.COMMAND_OFF:
					logging.info("Deactivating actuator...")
					statusCode = self._deactivateActuator(val = data.getValue(), stateData = data.getStateData())
				else:
					logging.warning("ActuatorData command is unknown. Ignoring: %s", str(curCommand))
					statusCode = -1
				
				# update the last known actuator command
				self.lastKnownCommand = curCommand
				
				# create the ActuatorData response from the original command
				actuatorResponse = ActuatorData()
				actuatorResponse.updateData(data)
				actuatorResponse.setStatusCode(statusCode)
				actuatorResponse.setAsResponse()
				
				return actuatorResponse
			
		return None
		
	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
		"""
		Should be implemented by sub-class.
		
		@param cmd The actuation command to process.
		@param stateData The string state data to use in processing the command.
		@return int The status code from the actuation call.
		"""
		pass
