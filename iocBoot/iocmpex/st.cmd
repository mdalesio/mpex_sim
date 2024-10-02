#!../../bin/linux-x86_64/mpex

#- You may have to change mpex to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/mpex.dbd"
mpex_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("db/vac_pmi.db")
dbLoadRecords("db/ttrain.db")
dbLoadRecords("db/sim.db")
dbLoadRecords("db/ui.db")


cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=user"
