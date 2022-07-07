import os
import time
from math import floor
from adafruit_rplidar import RPLidar

# start = time.time()  # 시작 시간 저장

# Setup the RPLidar
PORT_NAME = '/dev/tty.usbserial-0001'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0

def process_data(data):
    print(data)

scan_data = [0]*360
check = True
try:
    lidar = RPLidar(None, PORT_NAME, timeout=3)
#    print(lidar.get_info())  
    # start = time.time()  # 시작 시간 저장
    
    for scan in lidar.iter_scans():
        if check == False:
            break
        for (_, angle, distance) in scan:
            if (angle<45 or angle >270) and distance <500 :
                print(distance)
                check = False
                break

            else:
                continue

    end = time.time()

    # print(f"{end - start:.3f} sec")

    print("stop")
    lidar.stop_motor()
    lidar.stop()
    lidar.disconnect()


except:
    print('Stopping.')
    lidar.stop_motor()
    lidar.stop()
    lidar.disconnect()

# end = time.time()

# print(f"{end - start:.3f} sec")
