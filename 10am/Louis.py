from microbit import *

firework=Image('00000:00000:00000:00000:90000')
firework2=Image('00000:00000:00000:09000:60000')
firework3=Image('00000:00000:00900:06000:30000')
firework4=Image('00000:00000:00600:03000:00000')
firework5=Image('00000:00000:00300:00000:00000')
firework6=Image('00000:09090:00900:09090:00000')
firework7=Image('90909:09090:90909:09090:90909')
firework8=Image('90909:09090:90009:09090:90909')
firework9=Image('90909:00000:90009:00000:90909')
firework10=Image('60606:00000:60006:00000:60606')
firework11=Image('30303:00000:30003:00000:30303')
firework12=Image('00000:00000:00000:00000:00000')


def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br > 0:
                display.set_pixel(x,y,br-1)
            sleep(100)


fade()

while True:
    if button_a.was_pressed():
        display.show(firework)
        sleep(300)
        display.show(firework2)
        sleep(300)
        display.show(firework3)
        sleep(300)
        display.show(firework4)
        sleep(300)
        display.show(firework5)
        sleep(300)
        display.show(firework6)
        sleep(300)
        display.show(firework7)
        sleep(300)
        display.show(firework8)
        sleep(300)
        display.show(firework9)
        sleep(300)
        display.show(firework10)
        sleep(300)
        display.show(firework11)
        sleep(300)
        display.show(firework12)
        sleep(300)
