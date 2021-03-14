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
import os
import shutil 
from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask

class SystemDiskUtilTask(BaseSystemUtilTask):
    """
    Shell representation of class for student implementation.
    
    """

    def __init__(self):
        #pass
        """
        Initialization of class..
        
        """
        super(SystemDiskUtilTask, self).__init__()
    
    def _getSystemUtil(self) -> float:
        """
        returns Memory utilization value.
        
        """
        cwd = os.getcwd()
        total, used, free = shutil.disk_usage(cwd)
        cpu_per = used/total*100
        #return shutil.disk_usage(cwd)
        return cpu_per
        #pass
        