import RPi.GPIO as rp
from time import sleep

def d2b(a):
    return [int(bit) for bit in bin(a)[2:].zfill(8)]

def b2d(a):
    s = 0
    p = 1
    for i in range(8):
        s += a[7-i]*p
        p*=2
    return s


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = 15
comp = 4
troyka = 17
rp.setmode(rp.BCM)                           
rp.setup(dac, rp.OUT)
rp.setup(leds, rp.OUT)
rp.setup(troyka, rp.OUT, initial = rp.HIGH)
rp.setup(comp, rp.IN)

def adc():
    a = d2b(0)
    for i in range(8):
        a[i] = 1
        rp.output(dac, a)
        sleep(0.01)
        a[i] = rp.input(comp)
    return a


try:
    while True:
        u = b2d(adc())
        print(u/256*3.3)
        


finally:
    rp.output(dac, 0)
    rp.cleanup()