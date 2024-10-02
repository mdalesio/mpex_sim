from scan import *
from scan.util import SettingsBasedSet as Set
from scan.util import SettingsBasedWait as Wait

cmds_startrough = [
    Comment("Start Train Rough"),
    Set("VAC_PMIT:PMP:RPMP_req", 1),
    Delay(1),
    Comment("Rough Pump: Delayed"),
    Set("VAC_PMIT:VLV:BYP_req", 1),
    Wait("VAC_PMIT:VLV:BYP_sts", 1, timeout=5.0),
    Set("VAC_PMI:VLV:TTRAIN_req", 1),
    Wait("VAC_PMIT:VLV:BYP_sts", 1, timeout=5.0),
]

seq = CommandSequence(cmds_startrough)
scan_client = ScanClient()

print(scan_client)
id = scan_client.submit(seq, "Start Roughing")
print(cmds_startrough)
