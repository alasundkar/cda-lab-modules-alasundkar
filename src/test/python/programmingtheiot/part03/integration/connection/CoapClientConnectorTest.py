#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector

class CoapClientConnectorTest(unittest.TestCase):
	"""
	This test case class contains very basic integration tests for
	CoapClientConnector. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing CoapClientConnector class...")
		
		self.cfg = ConfigUtil()
		self.coapClient = CoapClientConnector()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	#@unittest.skip("Ignore for now.")
	def testConnectAndGet(self):
		self.coapClient.sendGetRequest(ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE)
		pass

	#@unittest.skip("Ignore for now.")
	def testConnectAndDelete(self):
		self.coapClient.sendDeleteRequest(ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE)
		pass

	#@unittest.skip("Ignore for now.")
	def testConnectAndPost(self):
		self.coapClient.sendPostRequest(ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE)
		pass

	#@unittest.skip("Ignore for now.")
	def testConnectAndPut(self):
		self.coapClient.sendPutRequest(ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE)
		pass

if __name__ == "__main__":
	unittest.main()
	