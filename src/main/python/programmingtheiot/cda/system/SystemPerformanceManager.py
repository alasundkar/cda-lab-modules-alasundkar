#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from apscheduler.schedulers.background import BackgroundScheduler

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData 
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask
from programmingtheiot.cda.system.SystemDiskUtilTask import SystemDiskUtilTask

class SystemPerformanceManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, pollRate: int = 30):
		#pass
		"""
		Initialization of class.
		
		@param pollRate integer value in seconds at which job should run
		"""
		self.cpuUtilTask = SystemCpuUtilTask()
		self.memUtilTask = SystemMemUtilTask()
		self.diskUtilTask = SystemDiskUtilTask()
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = pollRate)

	def handleTelemetry(self):
		"""
		fetches and logs CPU and memory util values
		
		"""
		#pass
		self.cpuUtilPct = self.cpuUtilTask.getTelemetryValue()
		self.memUtilPct = self.memUtilTask.getTelemetryValue()
		self.diskUtilPct = self.diskUtilTask.getTelemetryValue()
		logging.info('CPU utilization is %s percent,', str(self.cpuUtilPct))
		logging.info('Mem utilization is %s percent, ',str(self.memUtilPct))
		logging.info('Disk utilization is %s percent,', self.diskUtilPct)

		sysPerfData = SystemPerformanceData()
		#sysPerfData.setLocationID(self.locationID)
		sysPerfData.setCpuUtilization(self.cpuUtilPct)
		sysPerfData.setMemoryUtilization(self.memUtilPct)
		sysPerfData.setDiskUtilization(self.diskUtilPct)
		
				
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		pass
	
	def startManager(self):
		"""
		Starts the SystemPerformanceManager and scheduler.
		
		"""
		#pass
		logging.info("Started SystemPerformanceManager")
		self.scheduler.start()
		
	def stopManager(self):
		"""
		Stops the SystemPerformanceManager and scheduler.
		
		"""
		#pass
		logging.info("Stopped SystemPerformanceManager")
		self.scheduler.shutdown()