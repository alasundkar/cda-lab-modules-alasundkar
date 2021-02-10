#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import psutil

from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask

class SystemCpuUtilTask(BaseSystemUtilTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""
		Initialization of class..
		
		"""
		super(SystemCpuUtilTask, self).__init__()
	
	def _getSystemUtil(self) -> float:
		"""
		returns CPU utilization value.
		
		"""
		return psutil.cpu_percent()