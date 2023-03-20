import RPi.GPIO as rp
from time import sleep

def d2b(a):
    return [int(bit) for bit in bin(a)[2:].zfill(8)]

rp.setmode(rp.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
rp.setup(dac, rp.OUT)

T = 10
a = 0
p = 1

try:
    while True:
        rp.output(dac, d2b(a))
        sleep(T/512)
        a += p
        if a%255 == 0:
            p *= -1
        
        

finally:
    rp.output(dac, 0)
    rp.cleanup()