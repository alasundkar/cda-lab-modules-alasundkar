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
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, actuatorName = ConfigConst.NOT_SET, actuatorType: int = ConfigConst.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator"):
		pass
		
	def activateActuator(self, val: float) -> bool:
		pass
		
	def deactivateActuator(self) -> bool:
		pass
		
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
		pass
		
	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
		"""
		Should be implemented by sub-class.
		
		@param cmd The actuation command to process.
		@param stateData The string state data to use in processing the command.
		@return int The status code from the actuation call.
		"""
		pass
