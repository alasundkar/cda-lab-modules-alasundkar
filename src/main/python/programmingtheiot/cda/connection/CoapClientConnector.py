#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import socket
import traceback

from coapthon import defines
from coapthon.client.coap import CoAP
from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message
from coapthon.messages.request import Request
from coapthon.utils import parse_uri
from coapthon.utils import generate_random_token
from programmingtheiot.data.DataUtil import DataUtil
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
#import asyncio

#from aiocoap import *
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.cda.connection.IRequestResponseClient import IRequestResponseClient

class CoapClientConnector(IRequestResponseClient):
	"""
	Shell representation of class for student implementation.
	
	"""
	
# 	def __init__(self):
# 		pass
	def __init__(self, dataMsgListener: IDataMessageListener = None):
		self.config = ConfigUtil()
		self.dataMsgListener = dataMsgListener
		self.enableConfirmedMsgs = False
		self.coapClient = None
		
		self.observeRequests = { }
		
		self.host    = self.config.getProperty(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port    = self.config.getInteger(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_COAP_PORT)
		self.uriPath = "coap://" + self.host + ":" + str(self.port) + "/"
		
		logging.info('\tHost:Port: %s:%s', self.host, str(self.port))
		
		self.includeDebugLogDetail = True
		
		try:
			tmpHost = socket.gethostbyname(self.host)
			
			if tmpHost:
				self.host = tmpHost
				self._initClient()
			else:
				logging.error("Can't resolve host: " + self.host)
			
		except socket.gaierror:
			logging.info("Failed to resolve host: " + self.host)

	def _initClient(self):
		try:
			self.coapClient = HelperClient(server = (self.host, self.port))
	
			logging.info('Client created. Will invoke resources at: ' + self.uriPath)
		except Exception as e:
			# obviously, this is a critical failure - you may want to handle this differently
			logging.error("Failed to create CoAP client to URI path: " + self.uriPath)
			traceback.print_exception(type(e), e, e.__traceback__)
				
	
	"""
	sending discovery request for all resources and logging uri on callback method
	
	"""
	def sendDiscoveryRequest(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info('Discovering remote resources...')
		self.coapClient.get(path = '/.well-known/core', callback = self._onDiscoveryResponse, timeout = timeout)
		

	"""
	send delete request based on request type and logs payload and token as callback and returns true if successfull
	
	"""
	def sendDeleteRequest(self, resource: ResourceNameEnum, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info("sendDeleteRequest has been called..")
		if resource:
			logging.debug("Issuing DELETE with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.DELETE, path = resource.value)
			request.token = generate_random_token(2)
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, callback = self._onDeleteResponse, timeout = timeout)
		else:
			logging.warning("Can't test DELETE - no path or path list provided.")

	"""
	send get request based on request type and logs payload and token as callback and returns true if successfull
	
	"""
	def sendGetRequest(self, resource: ResourceNameEnum, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		if resource:
			logging.debug("Issuing GET with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.GET, path = resource.value)
			request.token = generate_random_token(2)
	
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, callback = self._onGetResponse, timeout = timeout)
		else:
			logging.warning("Can't test GET - no path or path list provided.")

	"""
	send post request based on request type and logs payload and token as callback and returns true if successfull
	
	"""
	def sendPostRequest(self, resource: ResourceNameEnum, payload = None, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info("sendPostRequest has been called..")
		if resource:
			logging.debug("Issuing POST with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.POST, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, callback = self._onPostResponse, timeout = timeout)
		else:
			logging.warning("Can't test POST - no path or path list provided.")

	"""
	send put request based on request type and logs payload and token as callback and returns true if successfull
	
	"""
	def sendPutRequest(self, resource: ResourceNameEnum, payload = None, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info("sendPutRequest has been called..")
		if resource:
			logging.debug("Issuing PUT with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.PUT, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
	
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, callback = self._onPutResponse, timeout = timeout)
		else:
			logging.warning("Can't test PUT - no path or path list provided.")

	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		self.dataMsgListener = listener
		
#	def startObserver(self, resource: ResourceNameEnum, ttl: int = IRequestResponseClient.DEFAULT_TTL) -> bool:
#		logging.info("startObserver has been called..")
		
	def startObserver(self, resource: ResourceNameEnum, name: str = None) -> bool:
		logging.info("startObserver has been called..")
		if resource or name:
			resourcePath = self._createResourcePath(resource, name)
		
		# TODO: track which resources are under observation
				
			try:
				self.coapClient.observe(path = resourcePath, callback = self._onGetResponse)
			except Exception as e:
				logging.warning("Failed to observe path: " + resource.value)
	
	def stopObserver(self, resource: ResourceNameEnum, name: str = None) -> bool:
		logging.info("startObserver has been called..")
				
		
	#def stopObserver(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
#		logging.info("stopObserver has been called..")

	def _createResourcePath(self, resource: ResourceNameEnum = None, name: str = None):
		resourcePath = ""
		
		hasResource = False
		
		if resource:
			resourcePath = resourcePath + resource.value
			hasResource = True
			
		if name:
			if hasResource:
				resourcePath = resourcePath + '/'
			
			resourcePath = resourcePath + name
		
		return resourcePath

	"""
	callback methods for get,put,post,delete methods which logs token,path and payload
	
	"""
	def _onGetResponse(self,response):
		logging.info('GET response received.')
		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
			resource = None
			
			if self.dataMsgListener:
				self.dataMsgListener.handleIncomingMessage(resource, str(response.payload))
	
	def _onPutResponse(self,response):
		logging.info('PUT response received.')
		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
			
	def _onPostResponse(self,response):
		logging.info('POST response received.')
		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
				
	def _onDeleteResponse(self,response):
		logging.info('DELETE response received.')
		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
