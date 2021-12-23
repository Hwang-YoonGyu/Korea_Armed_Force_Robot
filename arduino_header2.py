#<PWM Velocity Control Program>
#Left, Rignt Motor PWM Control

import RPi.GPIO as GPIO
import time
import sys

servo_pin = 18
servo_pin1 = 13
servo_pin2 = 12
servo_pin3 = 19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3.0)
GPIO.setup(servo_pin1, GPIO.OUT)
pwm1 = GPIO.PWM(servo_pin1, 50)
pwm1.start(3.0)
GPIO.setup(servo_pin2, GPIO.OUT)
pwm2 = GPIO.PWM(servo_pin2, 50)
pwm2.start(3.0)
GPIO.setup(servo_pin3, GPIO.OUT)
pwm3 = GPIO.PWM(servo_pin3, 50)
pwm3.start(3.0)

global servo1, servo2, servo3, servo4
servo1 = 3.0
servo2 = 3.0
servo3 = 3.0
servo4 = 4.5

def arm_left():
    global servo1
    servo1 -= 0.3
    if servo1 < 3.0:
        servo1 = 3.0
    elif servo1 > 9.5:
        servo1 = 9.5
    pwm.ChangeDutyCycle(servo1)
    time.sleep(1.0)
def arm_right():
    global servo1
    servo1 += 0.3
    if servo1 < 3.0:
        servo1 = 3.0
    elif servo1 > 9.5:
        servo1 = 9.5
    pwm.ChangeDutyCycle(servo1)
    time.sleep(1.0)
def arm1_up():
    global servo2
    servo2 += 0.3
    if servo2 < 3.0:
        servo2 = 3.0
    elif servo2 > 9.5:
        servo2 = 9.5
    pwm.ChangeDutyCycle(servo2)
    time.sleep(1.0)
def arm1_down():
    global servo2
    servo2 -= 0.3
    if servo2 < 3.0:
        servo2 = 3.0
    elif servo2 > 9.5:
        servo2 = 9.5
    pwm1.ChangeDutyCycle(servo2)
    time.sleep(1.0)
def arm2_up():
    global servo3
    servo3 += 0.3
    if servo3 < 3.0:
        servo3 = 3.0
    elif servo3 > 9.5:
        serv3 = 9.5
    pwm2.ChangeDutyCycle(servo3)
    time.sleep(1.0)
def arm2_down():
    global servo3
    servo3 -= 0.3
    if servo3 < 3.0:
        servo3 = 3.0
    elif servo3 > 9.5:
        servo3 = 9.5
    pwm2.ChangeDutyCycle(servo3)
    time.sleep(1.0)
def gripper_up():
    global servo4
    servo4 += 0.3
    if servo4 < 3.0:
        servo4 = 3.0
    elif servo4 > 9.5:
        servo4 = 9.5
    pwm3.ChangeDutyCycle(servo4)
    time.sleep(1.0)
def gripper_down():
    global servo4
    servo4 -= 0.3
    if servo4 < 3.0:
        servo4 = 3.0
    elif servo4 > 9.5:
        servo4 = 9.5
    pwm3.ChangeDutyCycle(servo4)
    time.sleep(1.0)

def allStop():
    pwm.ChangeDutyCycle(3.0)
    time.sleep(1.0)

#pwm.ChangeDutyCycle(0.0)
#pwm.stop()
#GPIO.cleanup()
