#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

"""
Configuration and other constants for use when looking up
configuration values or when default values may be needed.
 
"""

#####
# General Names and Defaults
#

NOT_SET = 'Not Set'

DEFAULT_HOST             = 'localhost'
DEFAULT_COAP_PORT        = 5683
DEFAULT_COAP_SECURE_PORT = 5684
DEFAULT_MQTT_PORT        = 1883
DEFAULT_MQTT_SECURE_PORT = 8883
DEFAULT_KEEP_ALIVE       = 60
DEFAULT_POLL_CYCLES      = 60
DEFAULT_VAL              = 0.0
DEFAULT_COMMAND          = 0
DEFAULT_STATUS           = 0

# for purposes of this library, float precision is more then sufficient
DEFAULT_LAT = DEFAULT_VAL
DEFAULT_LON = DEFAULT_VAL
DEFAULT_ELEVATION = DEFAULT_VAL

PRODUCT_NAME = 'PIOT'
CLOUD        = 'Cloud'
GATEWAY      = 'Gateway'
CONSTRAINED  = 'Constrained'
DEVICE       = 'Device'
SERVICE      = 'Service'

CONSTRAINED_DEVICE = CONSTRAINED + DEVICE
GATEWAY_SERVICE    = GATEWAY + SERVICE
CLOUD_SERVICE      = CLOUD + SERVICE

#####
# Property Names
#

NAME_PROP        = 'name'
TYPE_ID_PROP     = 'typeID'
TIMESTAMP_PROP   = 'timeStamp'
HAS_ERROR_PROP   = 'hasError'
STATUS_CODE_PROP = 'statusCode'
LOCATION_ID_PROP = 'locationID'
LATITUDE_PROP    = 'latitude'
LONGITUDE_PROP   = 'longitude'
ELEVATION_PROP   = 'elevation'

COMMAND_PROP     = 'command'
STATE_DATA_PROP  = 'stateData'
VALUE_PROP       = 'value'
IS_RESPONSE_PROP = 'isResponse'

CPU_UTIL_PROP    = 'cpuUtil'
DISK_UTIL_PROP   = 'diskUtil'
MEM_UTIL_PROP    = 'memUtil'

#####
# Resource and Topic Names
#

ACTUATOR_CMD      = 'ActuatorCmd'
ACTUATOR_RESPONSE = 'ActuatorResponse'
MGMT_STATUS_MSG   = 'MgmtStatusMsg'
MGMT_STATUS_CMD   = 'MgmtStatusCmd'
SENSOR_MSG        = 'SensorMsg'
SYSTEM_PERF_MSG   = 'SystemPerfMsg'

LED_ACTUATOR_NAME        = 'LedActuator'
HUMIDIFIER_ACTUATOR_NAME = 'HumidifierActuator'
HVAC_ACTUATOR_NAME       = 'HvacActuator'

HUMIDITY_SENSOR_NAME = 'HumiditySensor'
PRESSURE_SENSOR_NAME = 'PressureSensor'
TEMP_SENSOR_NAME     = 'TempSensor'

SYSTEM_PERF_NAME  = 'SystemPerformance'

COMMAND_OFF = DEFAULT_COMMAND
COMMAND_ON  = 1

DEFAULT_TYPE_ID           = 0
DEFAULT_ACTUATOR_TYPE     = DEFAULT_TYPE_ID
HVAC_ACTUATOR_TYPE        = 1
HUMIDIFIER_ACTUATOR_TYPE  = 2
LED_DISPLAY_ACTUATOR_TYPE = 100

DEFAULT_SENSOR_TYPE  = DEFAULT_TYPE_ID
HUMIDITY_SENSOR_TYPE = 1
PRESSURE_SENSOR_TYPE = 2
TEMP_SENSOR_TYPE     = 3

SYSTEM_PERF_TYPE     = 100
CPU_UTIL_TYPE        = 101
DISK_UTIL_TYPE       = 102
MEM_UTIL_TYPE        = 103

CPU_UTIL_NAME  = 'DeviceCpuUtil'
DISK_UTIL_NAME = 'DeviceDiskUtil'
MEM_UTIL_NAME  = 'DeviceMemUtil'

CDA_ACTUATOR_CMD_MSG_RESOURCE = PRODUCT_NAME + '/' + CONSTRAINED_DEVICE + '/' + ACTUATOR_CMD
CDA_ACTUATOR_RESPONSE_MSG_RESOURCE = PRODUCT_NAME + '/' + CONSTRAINED_DEVICE + '/' + ACTUATOR_RESPONSE
CDA_MGMT_STATUS_MSG_RESOURCE  = PRODUCT_NAME + '/' + CONSTRAINED_DEVICE + '/' + MGMT_STATUS_MSG
CDA_MGMT_CMD_MSG_RESOURCE     = PRODUCT_NAME + '/' + CONSTRAINED_DEVICE + '/' + MGMT_STATUS_CMD
CDA_SENSOR_DATA_MSG_RESOURCE  = PRODUCT_NAME + '/' + CONSTRAINED_DEVICE + '/' + SENSOR_MSG
CDA_SYSTEM_PERF_MSG_RESOURCE  = PRODUCT_NAME + '/' + CONSTRAINED_DEVICE + '/' + SYSTEM_PERF_MSG

#####
# Configuration Sections, Keys and Defaults
#

# NOTE: You may need to update these paths if you change
# the directory structure for python-components
DEFAULT_CONFIG_FILE_NAME = '../../../../../../../config/PiotConfig.props'
DEFAULT_CRED_FILE_NAME   = '../../../../../../../cred/PiotCred.props'

TEST_GDA_DATA_PATH_KEY = 'testGdaDataPath'
TEST_CDA_DATA_PATH_KEY = 'testCdaDataPath'

LOCAL   = 'Local'
MQTT    = 'Mqtt'
COAP    = 'Coap'
OPCUA   = 'Opcua'
SMTP    = 'Smtp'

DEVICE_LOCATION_ID_KEY = 'deviceLocationID'

CLOUD_GATEWAY_SERVICE = CLOUD   + '.' + GATEWAY_SERVICE
COAP_GATEWAY_SERVICE  = COAP    + '.' + GATEWAY_SERVICE
MQTT_GATEWAY_SERVICE  = MQTT    + '.' + GATEWAY_SERVICE
OPCUA_GATEWAY_SERVICE = OPCUA   + '.' + GATEWAY_SERVICE
SMTP_GATEWAY_SERVICE  = SMTP    + '.' + GATEWAY_SERVICE

CRED_SECTION = "Credentials"

FROM_ADDRESS_KEY     = 'fromAddr'
TO_ADDRESS_KEY       = 'toAddr'
TO_MEDIA_ADDRESS_KEY = 'toMediaAddr'
TO_TXT_ADDRESS_KEY   = 'toTxtAddr'

HOST_KEY             = 'host'
PORT_KEY             = 'port'
SECURE_PORT_KEY      = 'securePort'

USER_NAME_TOKEN_KEY  = 'userToken'
USER_AUTH_TOKEN_KEY  = 'authToken'
API_TOKEN_KEY        = 'apiToken'

CERT_FILE_KEY        = 'certFile'
CRED_FILE_KEY        = 'credFile'
ENABLE_AUTH_KEY      = 'enableAuth'
ENABLE_CRYPT_KEY     = 'enableCrypt'
ENABLE_EMULATOR_KEY  = 'enableEmulator'
ENABLE_SENSE_HAT_KEY = 'enableSenseHAT'
ENABLE_LOGGING_KEY   = 'enableLogging'
USE_WEB_ACCESS_KEY   = 'useWebAccess'
POLL_CYCLES_KEY      = 'pollCycleSecs'
KEEP_ALIVE_KEY       = 'keepAlive'
DEFAULT_QOS_KEY      = 'defaultQos'

ENABLE_MQTT_CLIENT_KEY = 'enableMqttClient'
ENABLE_COAP_CLIENT_KEY = 'enableCoapClient'
ENABLE_COAP_SERVER_KEY = 'enableCoapServer'

HUMIDITY_SIM_FLOOR_KEY   = 'humiditySimFloor'
HUMIDITY_SIM_CEILING_KEY = 'humiditySimCeiling'
PRESSURE_SIM_FLOOR_KEY   = 'pressureSimFloor'
PRESSURE_SIM_CEILING_KEY = 'pressureSimCeiling'
TEMP_SIM_FLOOR_KEY       = 'tempSimFloor'
TEMP_SIM_CEILING_KEY     = 'tempSimCeiling'

HANDLE_TEMP_CHANGE_ON_DEVICE_KEY = 'handleTempChangeOnDevice'
TRIGGER_HVAC_TEMP_FLOOR_KEY      = 'triggerHvacTempFloor'
TRIGGER_HVAC_TEMP_CEILING_KEY    = 'triggerHvacTempCeiling'
