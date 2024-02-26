
import L2_vector
import L1_log
import time
import numpy as np

while True:
    obs_meas = L2_vector.getNearest()
    L1_log.tmpFile(obs_meas[0], "Distances")
    L1_log.tmpFile(obs_meas[1], "Angles")
    print("Distance:",obs_meas[0], "Angles:", obs_meas[1])
    
    r = obs_meas[0]
    alpha = obs_meas[1]
    x = r * np.cos(alpha)                           # get x
    y = r * np.sin(alpha)                           # get y
    L1_log.tmpFile(x, "X") 
    L1_log.tmpFile(y, "Y")
    print("X:",x, "Y:", y)
    
    time.sleep(0.2)
