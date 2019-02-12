from microbit import *

sleep_delay = 200
firework=Image("00000:00000:00000:00000:50000")
fw2=Image("00000:00000:00000:05000:00000")
fw3=Image("00000:00000:00500:00000:00000")
fw4=Image("00000:00000:00900:00000:00000")
fw5=Image("00000:09090:00900:09090:00000")
fw6=Image("90909:09090:90909:09090:90909")
fw7=Image("99999:99999:99999:99999:99999")


def show_fw():
    display.show(firework)
    sleep(sleep_delay)
    display.show(fw2)
    sleep(sleep_delay)
    display.show(fw3)
    sleep(sleep_delay)
    display.show(fw4)
    sleep(sleep_delay)
    display.show(fw5)
    sleep(sleep_delay)
    display.show(fw6)
    sleep(sleep_delay)
    display.show(fw7)


def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
            sleep(10)


def fade_out():
    for j in range(0,9):
        fade()


while True:
    if button_a.was_pressed():
        show_fw()
        fade_out()
