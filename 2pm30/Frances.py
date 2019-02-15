from microbit import *
import music

firework1 = Image("00000:00000:00000:00000:00400")
firework2 = Image("00000:00000:00000:00600:00200")
firework3 = Image("00000:00000:00800:00400:00100")
firework4 = Image("00000:00900:00600:00200:00000")
firework5 = Image("98789:07670:00400:00100:00000")
firework6 = Image("98789:87678:00200:00000:00000")
firework7 = Image("98789:87678:90009:00000:00000")


def fade():
    for x in range(0,5):
        for y in range(0,5):
            #display.set_pixel(x,y,9)
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)              
        sleep(100)


while True:
    if button_a.was_pressed():
        display.show(firework1)
        sleep(100)
        display.show(firework2)
        sleep(100)
        display.show(firework3)
        sleep(100)
        display.show(firework4)
        sleep(100)
        display.show(firework5)
        sleep(100)
        display.show(firework6)
        sleep(100)
        display.show(firework7)
        music.play(music.ODE)
    fade()
