from RPi import GPIO
from time import sleep

'''
Mobility Class
--------------

Description
-----------
The mobility class controls the movement of a skidsteer robot. It uses the GPIO
module to link up to general purpose pins on a Raspberry Pi to control the motors
of the robot. There are four links:

l_forward -> Connection to the pin that moves the left motor forward

r_forward -> Connection to the pin that moves the right motor forward

l_reverse -> Connection to the pin that moves the left motor in reverse

r_reverse -> connection to the pin that moves the right motor in reverse

The is_set attribute determines if the pins have been set to recieve output.

Functions
-----------
forward -> moves the robot forward for a set amount of time (dur)

backward -> moves the robot backward for a set amount of time

turn_right -> turns the robot 90 degrees to the right, -pi/2

turn_left -> turns the robot 90 degrees to the left, pi/2

clean_up -> cleans up the GPIOs. Should be done when the robot is not in use

setup -> sets the pins up to OUTPUT mode to control the motors.

reset_pins -> resets the pins to a new GPIO set
'''

class Mobility():
    def __init__(self, l_forward, r_forward, l_reverse, r_reverse):
        self.l_forward = l_forward
        self.r_forward = r_forward
        self.l_reverse = l_reverse
        self.r_reverse = r_reverse

        self.is_set = False

        self.setup()

    def forward(self, dur):
        GPIO.output(self.l_forward, GPIO.HIGH)
        GPIO.output(self.r_forward, GPIO.HIGH)

        sleep(dur)

        GPIO.output(self.l_forward, GPIO.LOW)
        GPIO.output(slef.r_forward, GPIO.LOW)

    def backward(self, dur):
        GPIO.output(self.l_reverse, GPIO.HIGH)
        GPIO.output(self.r_reverse, GPIO.HIGH)

        sleep(dur)

        GPIO.output(self.l_reverse, GPIO.LOW)
        GPIO.output(self.r_reverse, GPIO.LOW)

    def turn_right(self):
        pass

    def turn_left(self):
        pass

    def clean_up(self):
        self.is_set = False
        GPIO.clean_up()

    def setup(self):
        self.is_set = True

        GPIO.setup(self.l_forward, GPIO.OUT)
        GPIO.setup(self.r_forward, GPIO.OUT)
        GPIO.setup(self.l_reverse, GPIO.OUT)
        GPIO.setup(self.r_reverse, GPIO.OUT)

    def reset_pins(self, new_l_for, new_r_for, new_l_rev, new_r_rev):
        self.clean_up()

        self.l_forward = new_l_for
        self.r_forward = new_r_for
        self.l_reverse = new_l_rev
        self.r_reverse = new_r_rev
