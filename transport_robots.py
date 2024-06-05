from pyatcrobo2.parts import *
from pystubit.board import *
from time import sleep
m1 = DCMotor('M1')
m2 = DCMotor('M2')
direction = 1

def setDirection(mode):
    global direction
    direction = mode

def setMotor(motor1, motor2):
    global m1
    global m2
    m1 = DCMotor(motor1)	
    m2 = DCMotor(motor2)   

def fd(mt):
    speed = mt*2.55
    m1.power(round(speed))
    m2.power(round(speed))
    if direction == 1:
        m1.ccw()
        m2.ccw()
    else:
        m1.cw()
        m2.cw()

def fd2(mtl,mtr):
    speed_L = mtl*2.55
    speed_R = mtr*2.55
    m1.power(round(speed_L))
    m2.power(round(speed_R))
    if direction == 1:
        m1.ccw()
        m2.ccw()
    else:
        m1.cw()
        m2.cw()

def bk(mt):
    speed = mt*2.55
    m1.power(round(speed))
    m2.power(round(speed))
    if direction == 1:
        m1.cw()
        m2.cw()
    else:
        m1.ccw()
        m2.ccw()

def bk2(mtl,mtr):
    speed_L = mtl*2.55
    speed_R = mtr*2.55
    m1.power(round(speed_L))
    m2.power(round(speed_R))
    if direction == 1:
        m1.cw()
        m2.cw()
    else:
        m1.ccw()
        m2.ccw()

def tl(mt):
    speed = mt*2.55
    m1.power(round(speed))
    if direction == 1:
        m1.ccw()
        m2.stop()
    else:
        m1.stop()
        m2.cw()
    
def tr(mt):
    speed = mt*2.55
    m2.power(round(speed))
    if direction == 1:
        m1.stop()
        m2.ccw()
    else:
        m1.cw()
        m2.stop()

def sl(mt):
    speed = mt*2.55
    m1.power(round(speed))
    m2.power(round(speed))
    m1.ccw()
    m2.cw()

def sr(mt):
    speed = mt*2.55
    m1.power(round(speed))
    m2.power(round(speed))
    m1.cw()
    m2.ccw()

def stop():
    m1.stop()
    m2.stop()

def wait_SWA():
    m1.stop()
    m2.stop()
    display.show('A',delay = 0,color=(display.RED))
    while not button_a.get_value()== 0:
        pass
    display.clear()

def wait_SWB():
    m1.stop()
    m2.stop()
    display.show('B',delay = 0,color=(display.RED))
    while not button_b.get_value()== 0:
        pass
    display.clear()

def wait_TouchSensor(p):
    m1.stop()
    m2.stop()
    SW = TouchSensor(p)
    display.show(str(p),delay = 0,color=(display.RED))
    while not SW.is_pressed():
        pass
    display.clear()
