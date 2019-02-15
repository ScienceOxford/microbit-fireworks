from microbit import *

def fade():
    for x in range(0,5):
        for y in range(0,5):
            br = display.get_pixel(x,y)
            if br > 0:
                display.set_pixel(x,y,br-1)
            sleep(10)


fireworka = Image('00000:00000:00000:00000:10000')
fireworkb = Image('00000:00000:00000:03000:10000')
fireworkc = Image('00000:00000:00600:03000:10000')
fireworkd = Image('00000:00090:00600:03000:10000')
firework = Image('00606:00090:00606:03000:10000')

display.show(fireworka)
sleep(100)
display.show(fireworkb)
sleep(100)
display.show(fireworkc)
sleep(100)
display.show(fireworkd)
sleep(100)
display.show(firework)
fade()
fade()
fade()
fade()
fade()
fade()
fade()
fade()
fade()
