#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import paho.mqtt.client as mqttClient

from programmingtheiot.common import ConfigUtil
from programmingtheiot.common import ConfigConst

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.IPubSubClient import IPubSubClient

DEFAULT_QOS = 1

class MqttClientConnector(IPubSubClient):
	"""
	Shell representation of class for student implementation.
	
	"""
	mqttClient = None
	clientID = None

	def __init__(self, clientID: str = None):
		"""
		Default constructor. This will set remote broker information and client connection
		information based on the default configuration file contents.
		
		@param clientID Defaults to None. Can be set by caller. If this is used, it's
		critically important that a unique, non-conflicting name be used so to avoid
		causing the MQTT broker to disconnect any client using the same name. With
		auto-reconnect enabled, this can cause a race condition where each client with
		the same clientID continuously attempts to re-connect, causing the broker to
		disconnect the previous instance.
		"""
		self.config = ConfigUtil.ConfigUtil()
		self.dataMsgListener = None
		
		self.host = self.config.getProperty(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port = self.config.getInteger( ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_MQTT_PORT)		
		self.keepAlive = self.config.getInteger( ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)		
		self.defaultQos = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.DEFAULT_QOS_KEY, self.DEFAULT_QOS)
		self.mqttClient = None		
		self.clientID = self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.DEVICE_LOCATION_ID_KEY, 'CDAMqttClientID001')
		
		logging.info('\tMQTT Client ID: ' + self.clientID)
		logging.info('\tMQTT Broker Host: ' + self.host)
		logging.info('\tMQTT Broker Port: ' + str(self.port))
		logging.info('\tMQTT Keep Alive:  ' + str(self.keepAlive))
		
		"""
		connects to client and returns true
	
		"""

	def connectClient(self) -> bool:
		if not self.mqttClient:
			# TODO: make clean_session configurable
			self.mqttClient = mqttClient.Client(client_id = self.clientID, clean_session = True)
			
			self.mqttClient.on_connect = self.onConnect
			self.mqttClient.on_disconnect = self.onDisconnect
			
			self.mqttClient.on_publish = self.onPublish
			self.mqttClient.on_subscribe = self.onSubscribe
			self.mqttClient.on_message = self.onMessage
		
		if not self.mqttClient.is_connected():
			self.mqttClient.connect(self.host, self.port, self.keepAlive)
			self.mqttClient.loop_start()
			return True
		else:
			logging.warn('MQTT client is already connected. Ignoring connect request.')
			return False
	
		"""
		Disconnects from client 
		
		"""	
	def disconnectClient(self) -> bool:
		if self.mqttClient.is_connected():
			self.mqttClient.loop_stop()
			self.mqttClient.disconnect()
		"""
		call back methods to implement functionalities after connect disconnect, on message received etc
	
		"""
			
	def onConnect(self, client, userdata, flags, rc):
		logging.info('client has successfully connected')		
		
	def onDisconnect(self, client, userdata, rc):
		logging.info('client has successfully disconnected')		
		
	def onMessage(self, client, userdata, msg):
		logging.info('onMessage has been called')
			
	def onPublish(self, client, userdata, mid):
		logging.info('onPublish has been called with message id : ' + mid)
	
	def onSubscribe(self, client, userdata, mid, granted_qos):
		logging.info('onSubscribe has been called with message id : ' + str(mid))

		
		"""
		publishes message to client after validation and returns true
	
		"""
	def publishMessage(self, resource: ResourceNameEnum, msg, qos: int = IPubSubClient.DEFAULT_QOS):
		logging.info('publishMessage has been called')
		if not resource:
			return False
		if qos < 0 or qos > 2:
			qos = IPubSubClient.DEFAULT_QOS
		logging.info('Message received is : ' + msg)
		self.mqttClient.publish(resource.name, msg, qos)
		return True	
		"""
		subscribes to topic and returns true
	
		"""	
	def subscribeToTopic(self, resource: ResourceNameEnum, qos: int = IPubSubClient.DEFAULT_QOS):
		logging.info('subscribeToTopic has been called')
		if not resource:
			return False
		if qos < 0 or qos > 2:
			qos = IPubSubClient.DEFAULT_QOS
		self.mqttClient.subscribe(resource.name, qos)
		return True
	
		"""
		Unsubscribes from topic
	
		"""	
	def unsubscribeFromTopic(self, resource: ResourceNameEnum):
		logging.info('unsubscribeToTopic has been called')
		self.mqttClient.unsubscribe(resource.name, None)

	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener:
			self.dataMsgListener = listener
