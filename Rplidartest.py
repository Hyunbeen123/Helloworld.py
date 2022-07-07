from rplidar import RPLidar
import time
from multiprocessing import Process
lidar = RPLidar('/dev/cu.usbserial-0001')
try:
    # info = lidar.get_info()
    # print(info)

    # health = lidar.get_health()
    # print(health)

    for i, scan in enumerate(lidar.iter_scans()):
        start = time.time()
        print('%d: Got %d measurments' % (i, len(scan)))
        
    # def multi(i, start, end):
        for i in scan:
        
            angle = str(i[1])
            distance = str(i[2])
            print('angle = '+str(i[1]))
            print('distance = '+str(i[2]))



        if (angle>45 or angle <180)and distance >2000:
                
            continue         
            # lidar.stop()
            # lidar.stop_motor()
            # lidar.disconnect()
        
        else:
        
            print("감지되었습니다")
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            




        print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    

except:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()