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
from programmingtheiot.common.ConfigUtil import ConfigUtil 
from programmingtheiot.common.IDataMessageListener import IDataMessageListener 
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator 
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask 
from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask 
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask 
from apscheduler.schedulers.background import BackgroundScheduler
#import logging

from importlib import import_module
from future.backports.test.pystone import FALSE
from programmingtheiot.cda.emulated import TemperatureSensorEmulatorTask
from pip._internal import self_outdated_check

#from apscheduler.schedulers.background import BackgroundScheduler

#from programmingtheiot.common.IDataMessageListener import IDataMessageListener

#from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
#from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask

class SensorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	
	"""
	Initializes all the three simulation tasks
	
	"""

	def __init__(self,useEmulator: bool = False):
#def __init__(self):  
		#self.useEmulator = useEmulator
		configUtil = ConfigUtil()
		self.humiditySensorSimTask = HumiditySensorSimTask() 
		self.pressureSensorSimTask = PressureSensorSimTask(self)
		self.temperatureSensorSimTask= TemperatureSensorSimTask()
		self.pollRate = configUtil.getInteger( section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.POLL_CYCLES_KEY, defaultVal = ConfigConst.DEFAULT_POLL_CYCLES)
		self.useEmulator = configUtil.getBoolean( section = ConfigConst.CONSTRAINED_DEVICE,key = ConfigConst.ENABLE_EMULATOR_KEY)
		self.locationID = configUtil.getProperty( section = ConfigConst.CONSTRAINED_DEVICE,  key = ConfigConst.DEVICE_LOCATION_ID_KEY, defaultVal = ConfigConst.NOT_SET) 
		self.dataMsgListener = None
   
		"""
		Creating a scheduler and adding a job to the scheduler for later execution
		"""
		self.scheduler = BackgroundScheduler()  
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = self.pollRate)

		if self.useEmulator == True:
			logging.info("Emulators will be used")
			"""
			Loading the Humidity Emulator
			"""
			humidityModule = __import__('programmingtheiot.cda.emulated.HumiditySensorEmulatorTask', fromlist = ['HumiditySensorEmulatorTask'])
			heClazz = getattr(humidityModule, 'HumiditySensorEmulatorTask')
			self.humidityEmulator = heClazz()
			
			"""
			Loading the Pressure Emulator
			"""
			pressureModule = __import__('programmingtheiot.cda.emulated.PressureSensorEmulatorTask', fromlist = ['PressureSensorEmulatorTask'])
			pressureAttribute = getattr(pressureModule, 'PressureSensorEmulatorTask')
			self.pressureEmulator = pressureAttribute()
			
			"""
			Loading the Temperature Emulator
			"""
			temperatureModule = __import__('programmingtheiot.cda.emulated.TemperatureSensorEmulatorTask', fromlist = ['TemperatureSensorEmulatorTask'])
			temperatureAttribute = getattr(temperatureModule, 'TemperatureSensorEmulatorTask')
			self.temperatureEmulator = temperatureAttribute()
		else:
			logging.info("Emulators will not be used")
			self.dataGenerator = SensorDataGenerator()
			configUtil = ConfigUtil()
			tempFloor = configUtil.getFloat(section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.TEMP_SIM_FLOOR_KEY, defaultVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP)
			tempCeiling = configUtil.getFloat(section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.TEMP_SIM_CEILING_KEY, defaultVal= SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
			humidityFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY)
			humidityCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
			pressureFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)
			pressureCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
			tempData = self.dataGenerator.generateDailyIndoorTemperatureDataSet(minValue = tempFloor, maxValue = tempCeiling, useSeconds = False)
			humidityData = self.dataGenerator.generateDailyEnvironmentHumidityDataSet( minValue= humidityFloor, maxValue = humidityCeiling, useSeconds=False)
			pressureData= self.dataGenerator.generateDailyEnvironmentPressureDataSet( minValue=pressureFloor, maxValue=pressureCeiling, useSeconds=False)

	"""
	handles sensor message and generates sensor data
	
	"""		        
	def handleTelemetry(self):
		
		if self.useEmulator == False:
			humiditySensorData = self.humiditySensorSimTask.generateTelemetry()
			pressureSensorData = self.pressureSensorSimTask.generateTelemetry()
			temperatureSensorData = self.temperatureSensorSimTask.generateTelemetry()
			self.dataMsgListener.handleSensorMessage(humiditySensorData)
			self.dataMsgListener.handleSensorMessage(pressureSensorData)
			self.dataMsgListener.handleSensorMessage(temperatureSensorData)
		else:
			humiditySensorData = self.humidityEmulator.generateTelemetry()
			pressureSensorData = self.pressureEmulator.generateTelemetry()
			temperatureSensorData = self.temperatureEmulator.generateTelemetry()
			self.dataMsgListener.handleSensorMessage(humiditySensorData)
			self.dataMsgListener.handleSensorMessage(pressureSensorData)
			self.dataMsgListener.handleSensorMessage(temperatureSensorData)

	"""
	check listener and return if its successful
	
	"""	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener:
			self.dataMsgListener = listener
			return True
		
		return False
	"""
	Starts Manager
	
	"""
	
	def startManager(self):  
		logging.info("Started SensorAdapterManager.")    
		if not self.scheduler.running:    
			self.scheduler.start()  
		else:    
			logging.warning("SensorAdapterManager scheduler already started.")
			
	"""
	Stops Manager
	
	"""			
	def stopManager(self):  
		logging.info("Stopped SensorAdapterManager.")    
		try:    
			self.scheduler.shutdown()  
		except:    
			logging.warning("SensorAdapterManager scheduler already stopped.")