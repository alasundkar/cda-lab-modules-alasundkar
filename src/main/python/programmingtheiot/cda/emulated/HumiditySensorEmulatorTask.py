#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData
import logging
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
from pisense import SenseHAT

class HumiditySensorEmulatorTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, dataSet = None):
		super(HumiditySensorEmulatorTask, self).__init__(SensorData.DEFAULT_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY, maxVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
		# Create an instance of SenseHAT and set the emulate flag to True if running the emulator, or False if using real hardware
		# This can be read from ConfigUtil using the ConfigConst.CONSTRAINED_DEVICE section and the ConfigConst.ENABLE_SENSE_HAT_KEY
		# If the ConfigConst.ENABLE_SENSE_HAT_KEY is False, set the emulate flag to True, otherwise set to False
		#self.sh = SenseHAT(emulate = enableEmulation)
		self.sh = SenseHAT(emulate = True)

		
	def generateTelemetry(self) -> SensorData:
		logging.info("inside HumiditySensorEmulatorTask ")
		sensorData = SensorData(typeID = self.sensorType)
		sensorVal = self.sh.environ.humidity	
		logging.info(sensorVal)
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData
		return sensorData
