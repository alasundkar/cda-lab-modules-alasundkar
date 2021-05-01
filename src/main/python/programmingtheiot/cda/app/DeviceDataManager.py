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
from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector
from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.cda.system.SensorAdapterManager import SensorAdapterManager
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager
from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DeviceDataManager(IDataMessageListener):
	"""
	Shell representation of class for student implementation.
	
	"""
	#enableMqtt = None
	enableCoap = None
	enableMqttClient = None
	mqttClient = None
	
	def __init__(self, enableMqtt: bool = True, enableCoap: bool = False):
		self.configUtil = ConfigUtil()
		self.dataUtil = DataUtil()
		self.enableCoap = enableCoap
		self.enableMqtt = enableMqtt
		#self.enableMqtt = ConfigConst.ENABLE_MQTT_CLIENT_KEY
		#self.enableMqtt = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_MQTT_CLIENT_KEY )
		"""
		Initializes sensor,actuator, system performance managers
	
		"""

		self.sensorAdapterManager = SensorAdapterManager()
		self.sensorAdapterManager.setDataMessageListener(self)

		self.systemPerformanceManager = SystemPerformanceManager()
		self.systemPerformanceManager.setDataMessageListener(self)
		
		self.actuatorAdapterManager = ActuatorAdapterManager()
		self.actuatorAdapterManager.setDataMessageListener(self)
		
		self.handleTempChangeOnDevice = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HANDLE_TEMP_CHANGE_ON_DEVICE_KEY)
		self.triggerHvacTempFloor = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_FLOOR_KEY)
		self.triggerHvacTempCeiling = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_CEILING_KEY);
		if self.enableMqtt is True:
			self.mqttClient = MqttClientConnector()
		
	def handleActuatorCommandMessage(self, data: ActuatorData) -> bool:
		if data:
			logging.info("Processing actuator command message.")
			self.actuatorAdapterManager.sendActuatorCommand(data)
			logging.info("And the command message is:")
			logging.info(self.dataUtil.actuatorDataToJson(data))
			return True
		else:
			logging.warning("Received invalid ActuatorData command message. Ignoring.")
			return False			
			
	def handleActuatorCommandResponse(self, data: ActuatorData) -> bool:
		"""
		Converts Actuator Data to json format from string format.
		@param data: ActuatorData 
		"""
		logging.info("Processing actuator command response")
		self.actuateData = DataUtil.actuatorDataToJson(self, data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_ACTUATOR_RESPONSE_RESOURCE, None)
		
	
	def handleIncomingMessage(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		"""
		Converts incoming json message to string format.
		@param resourceEnum: ResourceNameEnum
		@param msg: String message  
		"""
		logging.info("handleIncomingMessage initiated...")
		self._handleIncomingDataAnalysis(msg)
	
	def handleSensorMessage(self, data: SensorData) -> bool:
		"""
		Converts Sensor Message Data to json format from string format.
		@param data: SensorData data 
		"""
		logging.info("handleSensorMessage initiated...")
		self.sensorMessage = DataUtil.sensorDataToJson(self, data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, self.sensorMessage)
		self._handleSensorDataAnalysis(data)
	
	def handleSystemPerformanceMessage(self, data: SystemPerformanceData) -> bool:
		"""
		Converts System Performance Message to json format from string format.
		@param data: SystemPerformanceData data 
		"""
		logging.info("handleSystemPerformanceMessage has been initiated...")
		self.systemPerformanceMessage = DataUtil.systemPerformanceDataToJson(self, data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, self.systemPerformanceMessage)
	
	def startManager(self):
		"""
		Calls the start manager of SystemPerformanceManage and SensorAdapterManager. 
		"""
		logging.info("Device Data Manager is starting...")
		self.sensorAdapterManager.startManager()
		self.systemPerformanceManager.startManager()
		if self.mqttClient is not None:
			self.mqttClient.connectClient()
			logging.info("calling connectClient() DeviceDataManager...")

			self.mqttClient.subscribeToTopic(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, qos=1)
			self.mqttClient.subscribeToTopic(resource=ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, qos=1)
			self.mqttClient.subscribeToTopic(resource=ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, qos=1)
			self.mqttClient.subscribeToTopic(resource=ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, qos=1)
			self.mqttClient.subscribeToTopic(resource=ResourceNameEnum.CDA_MGMT_STATUS_CMD_RESOURCE, qos=1)

		
	def stopManager(self):
		"""
		Calls the start manager of SystemPerformanceManage and SensorAdapterManager. 
		"""
		logging.info("Device Data Manager is stopping...")
		self.sensorAdapterManager.stopManager()
		self.systemPerformanceManager.stopManager()
		if self.mqttClient is not None:
			self.mqttClient.unsubscribeFromTopic(resource=ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE)
			self.mqttClient.disconnectClient()
			
	def _handleIncomingDataAnalysis(self, msg: str):
		"""
		Call this from handleIncomeMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Validate msg: Most will be ActuatorData, but you may pass other info as well.
		2) Convert msg: Use DataUtil to convert if appropriate.
		3) Act on msg: Determine what - if any - action is required, and execute.
		"""
		logging.debug("_handleIncomingDataAnalysis initiated...")
		if self.validateJSON(msg) == True:
			self.actuatedData = DataUtil.jsonToActuatorData(self, msg)
			if(self.actuatedData < ConfigConst.HUMIDITY_SIM_FLOOR_KEY or self.actuatedData > ConfigConst.HUMIDITY_SIM_CEILING_KEY):
				self.actuateData.setValue(self.actuatedData)
				self.actuateData.setCommand(self.actuateData.COMMAND_ON)
						
	def _handleSensorDataAnalysis(self, data: SensorData):
		"""
		Call this from handleSensorMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Check config: Is there a rule or flag that requires immediate processing of data?
		2) Act on data: If # 1 is true, determine what - if any - action is required, and execute.
		"""
		logging.debug("_handleSensorDataAnalysis initiated...")
		if self.handleTempChangeOnDevice and data.getTypeID() == ConfigConst.TEMP_SENSOR_TYPE:        
			ad = ActuatorData(typeID = ConfigConst.HVAC_ACTUATOR_TYPE)        
			if data.getValue() > self.triggerHvacTempCeiling:      
				ad.setCommand(ConfigConst.COMMAND_ON)      
				ad.setValue(self.triggerHvacTempCeiling)    
			elif data.getValue() < self.triggerHvacTempFloor:      
				ad.setCommand(ConfigConst.COMMAND_ON)      
				ad.setValue(self.triggerHvacTempFloor)    
			else:      
				ad.setCommand(ConfigConst.COMMAND_OFF)        
				self.handleActuatorCommandMessage(ad)				
		
	def _handleUpstreamTransmission(self, resourceName: ResourceNameEnum, msg: str):
		"""
		Call this from handleActuatorCommandResponse(), handlesensorMessage(), and handleSystemPerformanceMessage()
		to determine if the message should be sent upstream. Steps to take:
		1) Check connection: Is there a client connection configured (and valid) to a remote MQTT or CoAP server?
		2) Act on msg: If # 1 is true, send message upstream using one (or both) client connections.
		"""
		logging.debug("_handleUpstreamTransmission initiated...")
		if self.enableMqtt is True:
			logging.debug("_handleUpstreamTransmission mqttClient  publishMessage has been called")
			logging.debug(resourceName.name)
			self.mqttClient.publishMessage(resourceName, msg, 1)
		if self.enableCoap is True:
			logging.debug("_handleUpstreamTransmission coapClient  sendPostRequest has been called")
			self.coapClient.sendPostRequest(resourceName, msg, 5)		