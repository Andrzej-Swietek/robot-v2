import time

class ultrasonic:
    def __init__(self, gpio, echo, trigger):
        self.echo = echo
        self.trigger = trigger
        self.gpio = gpio
    
    def utltraSonic(self,measure='cm'):
        try:
            self.gpio.setup(self.trigger, self.gpio.OUT)
            self.gpio.setup(self.echo, self.gpio.IN)

            self.gpio.output(self.trigger,False)
            while self.gpio.input(self.echo) == 0:
                nosig = timetim.time()
            while gpio.input(echo) == 1:
                sig = timetim.time()

            time_lenght = sig - nosig
            if measure == 'cm':
                distance = time_lenght / 0.000058 # dist in cm
            elif measure == 'in':
                distance = time_lenght / 0.000148 # dist in cm
            else:
                print('Unit Error')
                distance = none

            # gpio.cleanup()
            return distance

        except:
            distance = 100
            # gpio.cleanup()
            return distance