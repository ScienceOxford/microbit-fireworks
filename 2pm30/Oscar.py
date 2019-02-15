from microbit import *


def fade():
    for x in range(0,5): 
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
            sleep(5)


while True:
    if button_a.was_pressed():
        firework=Image("00090:90000:00900:00009:09000")
        display.show(firework)
        sleep(100)
        ggg=Image("00900:00000:90909:00000:00900")
        display.show(ggg)
        sleep(100)
        t=Image("09000:00009:00900:90000:00090")
        display.show(t)
        sleep(100)
        display.show(ggg)
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
    fade()
