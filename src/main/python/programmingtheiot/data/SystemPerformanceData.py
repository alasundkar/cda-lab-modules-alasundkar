#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask
from programmingtheiot.data.BaseIotData import BaseIotData

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	#CPU_Utilization = 0.0
	CPU_Utilization = 1
	Disk_Utilization = 1
	Memory_Utilization = 1
# 	Disk_Utilization = 0.0
# 	Memory_Utilization = 0.0
	#cpuUtil = ConfigConst.DEFAULT_VAL
	#diskUtil = 0.0
	#memUtil = ConfigConst.DEFAULT_VAL
	DEFAULT_VAL = 0.0
	
	def __init__(self, d = None):
		super(SystemPerformanceData, self).__init__(name = ConfigConst.SYSTEM_PERF_MSG, d = d)
		##pass
	
	def getCpuUtilization(self):
		"""
		Get CPU Utilization value
		"""
		return self.CPU_Utilization
	
	def getDiskUtilization(self):
		"""
		Get Disk Utilization value
		"""
		return self.Disk_Utilization
	
	def getMemoryUtilization(self):
		"""
		Get Memory Utilization Value
		"""
		return self.Memory_Utilization
	
	def setCpuUtilization(self, cpuUtil):
		"""
		Modifies the CPU utilization value for monitoring purpose
		@param cpuUtil: CPU utilization value
		"""
		self.CPU_Utilization = cpuUtil
		self.updateTimeStamp()
	
	def setDiskUtilization(self, diskUtil):
		"""
		Modifies Disk Utilization value for monitoring purpose
		@param diskUtil: Disk Utilization value 
		"""
		self.Disk_Utilization = diskUtil
	
	def setMemoryUtilization(self, memUtil):
		"""
		Modifies the Memory Utilization Value for monitoring purpose
		@param memUtil: Memory Utilization Value 
		"""
		self.Memory_Utilization = memUtil
		self.updateTimeStamp()
	
	def _handleUpdateData(self, data):
		"""
		Update the system performance data 
		@param data: updated system performance data 
		"""
		self.setCpuUtilization(data.getCpuUtilization())
		self.setDiskUtilization(data.getDiskUtilization())
		self.setMemoryUtilization(data.getMemoryUtilization())
