from microbit import *

firework=(Image("00000:00000:00900:00000:00000"))
sleep(300)
firework2=(Image("00000:07070:00900:07070:00000"))
display.show(firework2)
firework3=(Image("40004:07070:00900:07070:40004"))
sleep(300)
firework4=(Image("00000:00000:00400:07000:90000"))
display.show(firework4)
sleep(300)
firework5=(Image("00000:00000:00400:07070:90009"))
sleep(300)
display.show(firework5)
firework6=(Image("90000:07000:00400:07070:90009"))
sleep(300)
display.show(firework6)
firework7=(Image("90009:07070:00400:07070:90009"))
sleep(300)
display.show(firework7)


def fade():
    for x in range(2, 3):
        for y in range(2, 3):
            br = display.get_pixel(x, y)
            if br > 0:
                display.set_pixel(x, y, br-1)
            sleep(100)


while True:
    if button_a.was_pressed():
        display.show(firework)
        display.show(firework2)
        display.show(firework3)
        display.show(firework4)
        display.show(firework5)
        display.show(firework6)
        display.show(firework7)
    fade()
fade()
fade()
fade()
fade()
        
