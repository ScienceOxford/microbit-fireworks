from microbit import *

fire1=(Image("00000:00000:00000:00000:90000"))
fire2=(Image("00000:00000:00000:09000:00000"))
fire3=(Image("00000:00000:00900:00000:00000"))
fire4=(Image("00000:09090:00900:09090:00000"))
fire5=(Image("00900:09090:90909:09090:00900"))
fire6=(Image("90909:09090:90909:09090:90909"))


def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br > 0:
                display.set_pixel(x,y,br-1)


firework=[fire1,fire2,fire3,fire4,fire5,fire6]


while True:
    if button_a.was_pressed():
        display.show(firework,delay=200)
    sleep(200)
    fade()
