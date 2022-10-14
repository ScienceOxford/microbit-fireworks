from microbit import *

import music

firework = Image("00000:00000:00000:00000:00500")
firework2 = Image("00000:00000:00000:00500:00500")
firework3 = Image("00000:00000:00600:00600:00000")
firework4 = Image("00000:00700:00700:00000:00000")
firework5 = Image("00000:00800:08880:00800:00000")
firework6 = Image("00000:00800:08880:00800:00000")
firework7 = Image("00800:00000:80808:00000:00800")
firework8 = Image("00000:00000:00800:00000:00000")
firework9 = Image("90009:07070:00000:07070:90009")

while True:
         
    if button_a.was_pressed():
        
        music.play(music.ODE,wait=True)
        
    if button_b.was_pressed():
        
        display.show(firework,wait=True)
        sleep(100)

        display.show(firework2,wait=True)
        sleep(100)

        display.show(firework3,wait=True)
        sleep(100)

        display.show(firework4,wait=True)
        sleep(100)

        display.show(firework5,wait=True)
        sleep(100)

        display.show(firework6,wait=True)
        sleep(100)

        display.show(firework6,wait=True)
        sleep(100)

        display.show(firework7,wait=True)
        sleep(100)

        display.show(firework8,wait=True)
        sleep(100)

        display.show(firework9,wait=True)
        sleep(100)
