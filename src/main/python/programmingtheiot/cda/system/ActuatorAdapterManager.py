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
from programmingtheiot.common.ConfigUtil import ConfigUtil

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		#self.useEmulator = useEmulator
		configUtilObj = ConfigUtil()
		self.useEmulator = configUtilObj.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
		self.dataMsgListener = IDataMessageListener()
	#	self.locationID = ConfigConst.DEVICE_LOCATION_ID_KEY
		self.locationID = configUtilObj.getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.DEVICE_LOCATION_ID_KEY, defaultVal = ConfigConst.NOT_SET)
		if self.useEmulator == True:
			logging.info("Emulators will be used")
			"""
			Loading the Humidity Emulator
			"""
			humidifierModule = import_module('programmingtheiot.cda.emulated.HumidifierEmulatorTask', 'HumidifierEmulatorTask')
			hueClazz = getattr(humidifierModule, 'HumidifierEmulatorTask')
			self.humidifierEmulator = hueClazz()
			
			"""
			Loading the HVAC Emulator
			"""
			hvacModule = import_module('programmingtheiot.cda.emulated.HvacEmulatorTask', 'HvacEmulatorTask')
			hvacAttribute = getattr(hvacModule, 'HvacEmulatorTask')
			self.hvacEmulator = hvacAttribute()
			
			"""
			Loading the LED Emulator
			"""
			ledModule = import_module('programmingtheiot.cda.emulated.LedDisplayEmulatorTask','LedDisplayEmulatorTask')
			ledAttribute = getattr(ledModule, 'LedDisplayEmulatorTask')
			self.ledEmulator = ledAttribute()

		else:
			logging.info("Simulators will be used")
			# create the humidifier actuator
			self.humidifierActuator = HumidifierActuatorSimTask()
			# create the HVAC actuator
			self.hvacActuator = HvacActuatorSimTask()
	"""
	Sends Actuator command and return if its successfull
	
	"""			
		
	def sendActuatorCommand(self, data: ActuatorData) -> bool:
# 		if data and not data.isResponseFlagEnabled():    
# 			if data.getLocationID() is self.locationID:      
# 				logging.info("Processing actuator command for loc ID %s.", str(data.getLocationID()))
# 				aType = data.getTypeID()      
# 				responseData = None      
# 				if aType == ConfigConst.HUMIDIFIER_ACTUATOR_TYPE:        
# 					responseData = self.humidifierEmulator.updateActuator(data)      
# 				elif aType == ConfigConst.HVAC_ACTUATOR_TYPE:        
# 					responseData = self.hvacEmulator.updateActuator(data)      
# 				elif aType == ConfigConst.LED_DISPLAY_ACTUATOR_TYPE:        
# 					responseData = self.ledDisplayEmulator.updateActuator(data)      
# 				else:        
# 					logging.warning("No valid actuator type: %s", data.getTypeID())
# 				if responseData:        
# 					if self.dataMsgListener:          
# 						self.dataMsgListener.handleActuatorCommandResponse(responseData)
# 					return True    
# 			else:      
# 				logging.warning("Invalid loc ID match: %s", str(self.locationID))  
# 		else:    
# 			logging.warning("Invalid actuator msg. Response or null. Ignoring.") 
# 		return False



		if data != None and data.isResponseFlagEnabled() == False:
			self.dataMsgListener.handleActuatorCommandResponse(data)
 			
			"""
			Sends Humidifier or HVAC actuator commands based on the 'data' received.
			"""
			if self.useEmulator == False:
				if data.actuatorType == ActuatorData.HUMIDIFIER_ACTUATOR_TYPE:
					logging.info("Humidifier actuator initiated...")
					self.humidifierActuator.updateActuator(data)
				else:
					logging.info("HVAC actuator initiated...")
					self.hvacActuator.updateActuator(data)
				return True 
 					
			else:
				if data.actuatorType == ActuatorData.HUMIDIFIER_ACTUATOR_TYPE:
					logging.info("Humidifier actuator initiated...")
					self.humidifierEmulator.updateActuator(data)
				else:
					logging.info("HVAC actuator initiated...")
					self.hvacEmulator.updateActuator(data)
				return True 
		return False
					
	"""
	check listener and return if its successful
	
	"""		
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener:
			self.dataMsgListener = listener
			return True
		
		return False
