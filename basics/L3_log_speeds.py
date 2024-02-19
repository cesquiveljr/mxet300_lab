import L1_log
import L2_kinematics
import time

while True:
    dot = L2_kinematics.getMotion() #xdot and theta dot
    L1_log.tmpFile(dot[0], "X_dot") 
    L1_log.tmpFile(dot[1], "Theta_dot")

    speed = L2_kinematics.getPdCurrent() 
    L1_log.tmpFile(speed[0], "Left Wheel") #left wheel
    L1_log.tmpFile(speed[1], "Right Wheel") #right wheel
    print("X dot (m/s):", dot[0],"Theta dot (rad/s):", dot[1], "Chassis Speed (rad/s):", speed[0], "Wheel Speed (rad/s):", speed[1])
    time.sleep(0.2)

 