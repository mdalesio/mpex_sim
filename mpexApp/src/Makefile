TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = mpex
# mpex.dbd will be created and installed
DBD += mpex.dbd

# mpex.dbd will be made up from these files:
mpex_DBD += base.dbd

# Include dbd files from all support applications:
#mpex_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#mpex_LIBS += xxx

# mpex_registerRecordDeviceDriver.cpp derives from mpex.dbd
mpex_SRCS += mpex_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
mpex_SRCS_DEFAULT += mpexMain.cpp
mpex_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#mpex_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
mpex_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

