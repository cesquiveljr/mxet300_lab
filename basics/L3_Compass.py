import L2_compass_heading
import L1_oled
import L1_log
import time
deg = L2_compass_heading.get_heading()

def f1(): ## function for direction degree
    deg = L2_compass_heading.get_heading()
    print(deg)
    return deg

def f2(): ## function for direction
    x = "Undefined"
    if(-22.5 <= deg <= 22.5): 
        x = "N"
    elif(-67.5 <= deg <= -22.6):
        x = "NW"
    elif(-112.5 <= deg <= -67.6):
        x = "W"
    elif(-157.5 <= deg <=-112.6):
        x = "SW"
    elif(-157.6 <= deg <=157.6):
        x = "S"
    elif(67.5 <= deg <=22.6):
        x = "NE"
    elif(112.5 >= deg >= 67.6):
        x = "E"
    elif(157.5 >= deg >= 112.6):
        x = "SE"
    ##else:    
        ##print("Undefined")
    print(x)
    return x

while True:
    x = f2()
    deg = f1()
    direction = L1_log.stringTmpFile(x, "Cardinal_Direction")
    degree = L1_log.stringTmpFile(str(round((deg))), "Compass_Heading")
    time.sleep(1)  
    

        
    