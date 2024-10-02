TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = .
# ..dbd will be created and installed
DBD += ..dbd

# ..dbd will be made up from these files:
._DBD += base.dbd

# Include dbd files from all support applications:
#._DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#._LIBS += xxx

# ._registerRecordDeviceDriver.cpp derives from ..dbd
._SRCS += ._registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
._SRCS_DEFAULT += .Main.cpp
._SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#._OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
._LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

