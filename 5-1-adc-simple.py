import RPi.GPIO as rp
from time import sleep

def d2b(a):
    return [int(bit) for bit in bin(a)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]
aux = 15
comp = 4
troyka = 17    
rp.setmode(rp.BCM)                           
rp.setup(dac, rp.OUT)
rp.setup(troyka, rp.OUT, initial = rp.HIGH)
rp.setup(comp, rp.IN)

def adc():
    rp.output(dac, d2b(0))
    sleep(0.2)
    for i in range(0, 256):
        rp.output(dac, d2b(i))
        if rp.input(comp) == 0:
            return i
    return 255


try:
    while True:
        s = 0
        for i in range(3):
            s += adc()
        print(s/3/256*3.3)


finally:
    rp.output(dac, 0)
    rp.cleanup()