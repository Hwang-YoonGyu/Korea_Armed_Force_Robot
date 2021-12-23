#<PWM Velocity Control Program>
#Left, Rignt Motor PWM Control

import RPi.GPIO as GPIO
import time
import sys


L_DIR = 20
R_DIR = 21
F_DIR = 22

L_PWM = 12 #L_PWM L_DUTY 0~255(0~100%)
R_PWM = 13 #R_PWM R_DUTY 0~255(0~100%)
F_PWM = 18 #R_PWM R_DUTY 0~255(0~100%)


GPIO.setmode(GPIO.BCM)# GPIO Numbering
GPIO.setwarnings(False)

GPIO.setup(L_DIR,GPIO.OUT)  # All pins as Outputs
GPIO.setup(R_DIR,GPIO.OUT)
GPIO.setup(F_DIR,GPIO.OUT)

GPIO.setup(L_PWM,GPIO.OUT)
GPIO.setup(R_PWM,GPIO.OUT)
GPIO.setup(F_PWM,GPIO.OUT)

L_DUTY = GPIO.PWM(L_PWM,70)
R_DUTY = GPIO.PWM(R_PWM,70)
F_DUTY = GPIO.PWM(F_PWM,100)

L_DUTY.start(0)
R_DUTY.start(0)
F_DUTY.start(0)


def MStop():
    L_DUTY.ChangeDutyCycle(0)
    R_DUTY.ChangeDutyCycle(0)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(1)

def MGo1():
    L_DUTY.ChangeDutyCycle(11.5)
    R_DUTY.ChangeDutyCycle(10)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def MGo2():
    L_DUTY.ChangeDutyCycle(21.5)
    R_DUTY.ChangeDutyCycle(20)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def MGo3():
    L_DUTY.ChangeDutyCycle(31.5)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def MGo4():
    L_DUTY.ChangeDutyCycle(41.5)
    R_DUTY.ChangeDutyCycle(40)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MGo5():
    L_DUTY.ChangeDutyCycle(51.5)
    R_DUTY.ChangeDutyCycle(50)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MGo6():
    L_DUTY.ChangeDutyCycle(61.5)
    R_DUTY.ChangeDutyCycle(60)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MGo7():
    L_DUTY.ChangeDutyCycle(71.5)
    R_DUTY.ChangeDutyCycle(70)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MGo8():
    L_DUTY.ChangeDutyCycle(81.5)
    R_DUTY.ChangeDutyCycle(80)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MGo9():
    L_DUTY.ChangeDutyCycle(91.5)
    R_DUTY.ChangeDutyCycle(90)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MBack1():
    L_DUTY.ChangeDutyCycle(12)
    R_DUTY.ChangeDutyCycle(10)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack2():
    L_DUTY.ChangeDutyCycle(22)
    R_DUTY.ChangeDutyCycle(20)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack3():
    L_DUTY.ChangeDutyCycle(32)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack4():
    L_DUTY.ChangeDutyCycle(42)
    R_DUTY.ChangeDutyCycle(40)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack5():
    L_DUTY.ChangeDutyCycle(52)
    R_DUTY.ChangeDutyCycle(50)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack6():
    L_DUTY.ChangeDutyCycle(62)
    R_DUTY.ChangeDutyCycle(60)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack7():
    L_DUTY.ChangeDutyCycle(72)
    R_DUTY.ChangeDutyCycle(70)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack8():
    L_DUTY.ChangeDutyCycle(82)
    R_DUTY.ChangeDutyCycle(80)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MBack9():
    L_DUTY.ChangeDutyCycle(92)
    R_DUTY.ChangeDutyCycle(90)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MLeft1():
    L_DUTY.ChangeDutyCycle(20)
    R_DUTY.ChangeDutyCycle(40)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft2():
    L_DUTY.ChangeDutyCycle(20)
    R_DUTY.ChangeDutyCycle(50)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft3():
    L_DUTY.ChangeDutyCycle(20)
    R_DUTY.ChangeDutyCycle(60)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft4():
    L_DUTY.ChangeDutyCycle(20)
    R_DUTY.ChangeDutyCycle(70)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft5():
    L_DUTY.ChangeDutyCycle(30)
    R_DUTY.ChangeDutyCycle(50)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft6():
    L_DUTY.ChangeDutyCycle(30)
    R_DUTY.ChangeDutyCycle(60)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft7():
    L_DUTY.ChangeDutyCycle(30)
    R_DUTY.ChangeDutyCycle(70)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft8():
    L_DUTY.ChangeDutyCycle(40)
    R_DUTY.ChangeDutyCycle(60)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeft9():
    L_DUTY.ChangeDutyCycle(40)
    R_DUTY.ChangeDutyCycle(70)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeftSpin1():
    L_DUTY.ChangeDutyCycle(30)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeftSpin2():
    L_DUTY.ChangeDutyCycle(30)
    R_DUTY.ChangeDutyCycle(50)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MLeftSpin3():
    L_DUTY.ChangeDutyCycle(50)
    R_DUTY.ChangeDutyCycle(50)
    GPIO.output(L_DIR,GPIO.LOW)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight1():
    L_DUTY.ChangeDutyCycle(40)
    R_DUTY.ChangeDutyCycle(20)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight2():
    L_DUTY.ChangeDutyCycle(50)
    R_DUTY.ChangeDutyCycle(20)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight3():
    L_DUTY.ChangeDutyCycle(60)
    R_DUTY.ChangeDutyCycle(20)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight4():
    L_DUTY.ChangeDutyCycle(70)
    R_DUTY.ChangeDutyCycle(20)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight5():
    L_DUTY.ChangeDutyCycle(50)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight6():
    L_DUTY.ChangeDutyCycle(60)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight7():
    L_DUTY.ChangeDutyCycle(70)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight8():
    L_DUTY.ChangeDutyCycle(60)
    R_DUTY.ChangeDutyCycle(40)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRight9():
    L_DUTY.ChangeDutyCycle(70)
    R_DUTY.ChangeDutyCycle(40)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    #time.sleep(0.5)
def MRightSpin1():
    L_DUTY.ChangeDutyCycle(30)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MRightSpin2():
    L_DUTY.ChangeDutyCycle(50)
    R_DUTY.ChangeDutyCycle(30)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)
def MRightSpin3():
    L_DUTY.ChangeDutyCycle(50)
    R_DUTY.ChangeDutyCycle(50)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FStop():
    F_DUTY.ChangeDutyCycle(0)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo1():
    F_DUTY.ChangeDutyCycle(10)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo2():
    F_DUTY.ChangeDutyCycle(20)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo3():
    F_DUTY.ChangeDutyCycle(30)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo4():
    F_DUTY.ChangeDutyCycle(40)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo5():
    F_DUTY.ChangeDutyCycle(50)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo6():
    F_DUTY.ChangeDutyCycle(60)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo7():
    F_DUTY.ChangeDutyCycle(70)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo8():
    F_DUTY.ChangeDutyCycle(80)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FGo9():
    F_DUTY.ChangeDutyCycle(90)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(0.5)

def FBack1():
    F_DUTY.ChangeDutyCycle(10)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack2():
    F_DUTY.ChangeDutyCycle(20)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack3():
    F_DUTY.ChangeDutyCycle(30)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack4():
    F_DUTY.ChangeDutyCycle(40)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack5():
    F_DUTY.ChangeDutyCycle(50)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack6():
    F_DUTY.ChangeDutyCycle(60)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack7():
    F_DUTY.ChangeDutyCycle(70)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack8():
    F_DUTY.ChangeDutyCycle(80)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def FBack9():
    F_DUTY.ChangeDutyCycle(90)
    GPIO.output(F_DIR,GPIO.LOW)
    #time.sleep(0.5)

def AllStop():
    L_DUTY.ChangeDutyCycle(0)
    R_DUTY.ChangeDutyCycle(0)
    F_DUTY.ChangeDutyCycle(0)
    GPIO.output(L_DIR,GPIO.HIGH)
    GPIO.output(R_DIR,GPIO.HIGH)
    GPIO.output(F_DIR,GPIO.HIGH)
    #time.sleep(1)

def destroy():
    L_DUTY.stop()
    R_DUTY.stop()
    F_DUTY.stop()
    GPIO.cleanup()
    sys.exit()

def delay(t):
    time.sleep(t)

if __name__ == '__main__':     # Program start from here
    try:
        MStop(3)
        MGo1()
        MStop(1)
        MBack1()
        MStop(1)
        MLeft()
        MStop(1)
        MRight1()
        MStop(99999999)
    except KeyboardInterrupt:
