from mpu6050 import mpu6050
import RPi.GPIO as GPIO


class Robot:
    def __init__(self):
        self.motor1a = 7
        self.motor1b = 11
        # self.mpu = mpu6050(0x68)
        self.motor2a = 13
        self.motor2b = 16

        GPIO.cleanup()
        GPIO.setup(motor1a,GPIO.OUT)
        GPIO.setup(motor1b,GPIO.OUT)
        GPIO.setup(motor2a,GPIO.OUT)
        GPIO.setup(motor2b,GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        pwm=GPIO.PWM(21, 50)
        pwm.start(0)

    def turnRight(self):
        GPIO.output(motor1a,GPIO.HIGH)
        GPIO.output(motor1b,GPIO.LOW)
        GPIO.output(motor2a,GPIO.HIGH)
        GPIO.output(motor2b,GPIO.LOW)
        print("turning Right")

    def turnLeft(self):
        GPIO.output(motor1a,GPIO.LOW)
        GPIO.output(motor1b,GPIO.HIGH)
        GPIO.output(motor2a,GPIO.LOW)
        GPIO.output(motor2b,GPIO.HIGH)
        print("turning Left")

    def goStreight(self):
        GPIO.output(motor1a,GPIO.HIGH)
        GPIO.output(motor1b,GPIO.LOW)
        GPIO.output(motor2a,GPIO.LOW)
        GPIO.output(motor2b,GPIO.HIGH)
        print("GO STERIGHT")

    def goBackwards(self):
        GPIO.output(motor1a,GPIO.LOW)
        GPIO.output(motor1b,GPIO.HIGH)
        GPIO.output(motor2a,GPIO.HIGH)
        GPIO.output(motor2b,GPIO.LOW)
        print("GO BACKWORDS")

    def stop(self):
        GPIO.output(21, True)
        pwm.ChangeDutyCycle(0)
        GPIO.output(motor1a,GPIO.LOW)
        GPIO.output(motor1b,GPIO.LOW)
        GPIO.output(motor2a,GPIO.LOW)
        GPIO.output(motor2b,GPIO.LOW)
        print("STOP")
