#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from pisense import SenseHAT

class TemperatureSensorEmulatorTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

#	def __init__(self, dataSet = None):
#		super(TemperatureSensorEmulatorTask, self).__init__(SensorData.TEMP_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP, maxVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
	def __init__(self, dataSet = None):
		super(TemperatureSensorEmulatorTask, self).__init__(sensorName = ConfigConst.TEMP_SENSOR_NAME, sensorType = ConfigConst.TEMP_SENSOR_TYPE, dataSet = dataSet, minVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP, maxVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
		configUtil = ConfigUtil()
	#	self.name = ConfigConst.TEMP_SENSOR_NAME
		self.enableEmulator = configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY, False)
		if self.enableEmulator:
			enableEmulation = False
		else:
			enableEmulation = True
			self.sh = SenseHAT(emulate = enableEmulation)
			
	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(typeID = self.sensorType)
		sensorVal = self.sh.environ.temperature		
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData
		return sensorData
