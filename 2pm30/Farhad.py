from microbit import *

the_winning_firework=Image("90909:09990:99999:09990:90909")
display.show(the_winning_firework)
sleep(500)

def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
        sleep(100)
fade()

import music
music.play(music.BIRTHDAY)


the_winning_firework2=Image("00900:09090:90909:09090:00900")
display.show(the_winning_firework2)
sleep(500)

def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
        sleep(100)
fade()

import music
music.play(music.BIRTHDAY)


win_FIREWORK3=Image("90009:09090:90909:09090:90909")
display.show(win_FIREWORK3)

import music
music.play(music.BIRTHDAY)

def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
        sleep(100)
fade()


while True:
    if button_b.was_pressed():
        display.show(the_winning_firework)
        sleep(1000)
        display.show(the_winning_firework2)
        sleep(1000)
        display.show(win_firework3)
        sleep(1000)
    fade()
