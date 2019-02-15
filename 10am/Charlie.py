from microbit import *

firework=Image("90909:09090:90909:09090:90909")
display.show(firework)
sleep(500)
firework=Image("09090:909090:09090:90909:09090")
display.show(firework)
sleep(500)
firework=Image("00000:009000:09990:00900:00000")
display.show(firework)
sleep(600)
firework=Image("90009:00000:00000:00000:90009")
display.show(firework)
sleep(500)
firework=Image("00800:00000:70707:00000:00800")
display.show(firework)
sleep(100)


def fade():
    for x in range(1, 5):
        for y in range(1, 3):
            br = display.get_pixel(x, y)
            if br > 3:
                display.set_pixel(x, y, br-1)
        sleep(100)


fade()
fade()
fade()
fade()


while True:
    if button_a.was_pressed():
        display.show(firework)
    fade()
