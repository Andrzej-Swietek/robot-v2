from flask import Flask, render_template
from flask_socketio import SocketIO, send
from robot import Robot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor:
    def __init__(self, en, in1, in2):
        self.ena = en
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(en, GPIO.out)
        GPIO.setup(in1, GPIO.out)
        GPIO.setup(in2, GPIO.out)
        self.pwm = GPIO.pwm(self.ena, 100)
        self.pwm.start(0)

    def move_forward(self, speed=100):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)

    def move_backward(self, speed=100):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'zaq1@WSX'
socketio = SocketIO(app, cors_allowed_origins='*')
# robot = Robot()

motor_a = Motor(2, 3, 4)
motor_b = Motor(17, 27, 22)

IP_ADDRESS = '192.168.43.101'
PORT = 5000


@socketio.on('message')
def message(msg):
    print('Message : ' + msg)
    send(msg, broadcast=True)
    if msg == 'up':
        motor_a.move_forward()
        motor_b.move_forward()

    elif msg == 'back':
        motor_a.move_backward()
        motor_b.move_backward()

    elif msg == 'right':
        motor_a.move_backward()
        motor_b.move_forward()

    elif msg == 'left':
        motor_a.move_forward()
        motor_b.move_backward()

    elif msg == 'stop':
        motor_a.stop()
        motor_b.stop()


@app.route('/', methods=["GET"])
def client():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run()
    socketio.run(app, host=IP_ADDRESS,port=PORT)
