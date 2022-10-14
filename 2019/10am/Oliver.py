from microbit import *

#firework = Image("55555:55555:55555:55555:55555")
#sleep(100)
#firework = Image.HAPPY
#firework = Image.HEART
#firework = Image.SAD

firework = Image("05950:59995:59995:03930:01910")

#firework = Image("92429:28682:46864:28682:92429")
#firework = Image("05050:59995:95959:09590:00900")

display.show(firework)


def fade():
    for x in range(0, 5):
        for y in range(0, 5):
            # display.set_pixel(y,x,3)
            br = display.get_pixel(x, y)
            if br > 0:
                display.set_pixel(x, y, br-1)
            sleep(100)


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

while True:
    if button_a.was_pressed():
        display.show(firework)
        fade()

    if button_b.was_pressed():
        display.show(firework)
        fade()

    if accelerometer.was_gesture("shake"):
        display.show(firework)
        fade()
