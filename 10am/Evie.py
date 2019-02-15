from microbit import *

#firework=Image("90009:09090:99999:09090:90009")
firework=Image("90909:09990:99099:09990:90909")


def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
            sleep(50)


while True:
    if button_b.was_pressed():
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
