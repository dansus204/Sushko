import RPi.GPIO as rp

def d2b(a):
    return [int(bit) for bit in bin(a)[2:].zfill(8)]

rp.setmode(rp.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
rp.setup(dac, rp.OUT)

s = input("Введите целое число от 0 до 255: ")
try:
    while s != 'q':
        try:
            a = int(s)
        except ValueError:
            try:
                a = float(s)
            except ValueError:
                print("Это не число.")
            else:
                print("Это не целое число.")
        else:
            if a > 255:
                print("Число больше 255")
            elif a < 0:
                print("Число меньше нуля")
            else:
                rp.output(dac, d2b(a))
                print("Предполагаемое напряжение:", 3.3*a/256)

        finally:
            s = input("Введите целое число от 0 до 255: ")

finally:
    rp.output(dac, 0)
    rp.cleanup()