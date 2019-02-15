from microbit import *

firework=Image("90009:09090:00900:09090:90009")
display.show(firework)
sleep(100)


def fade():
    for x in range(0,5):
        for y in range(0,5):
            #display.set_pixel(y,x,9)
            br = display.get_pixel(x, y)
            if br > 0:
                display.set_pixel(x, y, br-1)
            sleep(20)


while True:
    if button_a.was_pressed():
        display.show(firework)
    fade()
