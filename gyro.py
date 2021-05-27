# sudo apt install python3-smbus
# pip install mpu6050-raspberrypi
# i w raspi-config zeneblowac i2c cos tam
from mpu6050 import mpu6050
import time

class Gyro:
    def __init__(self):
        mpu = mpu6050(0x68)
        temperature = 0
        accel_x = 0
        accel_y = 0
        accel_z = 0

        gyro_x = 0
        gyro_y = 0
        gyro_z = 0

    def update(self):
        """
            Function to be exectued in main interval / loop
        """
        print("Temp : "+str(self.mpu.get_temp()))
        print()

        accel_data = self.mpu.get_accel_data()
        print("Acc X : "+str(accel_data['x']))
        print("Acc Y : "+str(accel_data['y']))
        print("Acc Z : "+str(accel_data['z']))
        print()

        gyro_data = self.mpu.get_gyro_data()
        print("Gyro X : "+str(gyro_data['x']))
        print("Gyro Y : "+str(gyro_data['y']))
        print("Gyro Z : "+str(gyro_data['z']))
        print()
        print("-------------------------------")

        return { 
            "temp": self.temperature ,
            "accel_x": self.accel_x, 
            "accel_y": self.accel_y, 
            "accel_z": self.accel_z, 
            "gyro_x": self.gyro_x,
            "gyro_y": self.gyro_y,
            "gyro_z": self.gyro_z
            }
        time.sleep(1)