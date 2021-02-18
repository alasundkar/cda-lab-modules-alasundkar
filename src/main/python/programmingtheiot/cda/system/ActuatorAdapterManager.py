#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
from importlib import import_module
from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask
from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self,useEmulator: bool = True):
		#self.useEmulator = useEmulator
		self.useEmulator =ConfigConst.ENABLE_EMULATOR_KEY
		self.dataMsgListener = IDataMessageListener()
		self.locationID = ConfigConst.DEVICE_LOCATION_ID_KEY
		if self.useEmulator == True:
			logging.info("Emulators will be used")

		else:
			logging.info("Simulators will be used")
			# create the humidifier actuator
			self.humidifierActuator = HumidifierActuatorSimTask()
			# create the HVAC actuator
			self.hvacActuator = HvacActuatorSimTask()
		
	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		if data and not data.isResponseFlagEnabled():    
			if data.getLocationID() is self.locationID:      
				logging.info("Processing actuator command for loc ID %s.", str(data.getLocationID()))
				aType = data.getTypeID()      
				responseData = None      
				if aType == ConfigConst.HUMIDIFIER_ACTUATOR_TYPE:        
					responseData = self.humidifierEmulator.updateActuator(data)      
				elif aType == ConfigConst.HVAC_ACTUATOR_TYPE:        
					responseData = self.hvacEmulator.updateActuator(data)      
				elif aType == ConfigConst.LED_DISPLAY_ACTUATOR_TYPE:        
					responseData = self.ledDisplayEmulator.updateActuator(data)      
				else:        
					logging.warning("No valid actuator type: %s", data.getTypeID())
				if responseData:        
					if self.dataMsgListener:          
						self.dataMsgListener.handleActuatorCommandResponse(responseData)
					return True    
			else:      
				logging.warning("Invalid loc ID match: %s", str(self.locationID))  
		else:    
			logging.warning("Invalid actuator msg. Response or null. Ignoring.") 
		return False	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener:
			self.dataMsgListener = listener
			return True
		
		return False
