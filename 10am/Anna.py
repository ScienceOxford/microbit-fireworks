from microbit import *
firework1 = Image("00000:00000:00400:00000:00000")
firework2 = Image("00000:00000:44444:00000:00000")
firework3 = Image("00000:00400:44444:00400:00000")
firework4 = Image("00500:00500:55555:00500:00500")
firework5 = Image("00700:00770:77777:07700:00700")
firework6 = Image("90909:09990:99999:09990:90909")


def fade():
    for x in range(0,5):
        for y in range(0,5):
            br = display.get_pixel(x,y)
            if br > 0:
                display.set_pixel(x, y, br-1)
            sleep(10)


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
    fade() 
    fade()
    fade()
    fade()
    fade()
    fade()
    fade()
    fade()
