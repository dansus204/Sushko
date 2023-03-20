import RPi.GPIO as rp

rp.setmode(rp.BCM)
aux = 15

rp.setup(aux, rp.OUT)

A = 0

fr = 1000
p = rp.PWM(aux, fr)
dc = 0
p.start(dc)

try:
    while True:
        dc = int(input())
        p.ChangeDutyCycle(dc)

finally:
    rp.output(dac, 0)
    rp.cleanup()