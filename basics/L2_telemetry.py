
import L1_ina
import L1_log
import time

while True:
    myBatt = round(L1_ina.readVolts(),2)       # collect a reading
    L1_log.tmpFile(myBatt, "voltage")
    time.sleep(1)                       # pause