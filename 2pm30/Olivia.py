from microbit import *
import music

music.play(music.ODE)

firework=Image("12345:23456:34567:45678:56789")
firework2=Image("23456:34567:45678:56789:45678")
firework3=Image("34567:45678:56789:45678:34567")
firework4=Image("99999:99999:99999:99999:99999")
firework5=Image("22222:55555:99999:55555:22222")


def fade():
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
        sleep(100)


while True:
    if button_a.was_pressed():
        import music
        music.play(music.ENTERTAINER)
        display.show(firework)
        sleep(1000)
        display.show(firework2)
        sleep(1000)
        display.show(firework3)
        sleep(1000)
        display.show(firework4)
        sleep(500)
        display.show(firework5)
        sleep(500)
        fade()
        sleep(100)
        fade()
        sleep(100)
        fade()
        sleep(100)
        fade()
        sleep(100)
        fade()
        sleep(100)
        fade()
        sleep(100)
        fade()
        sleep(100)
        fade()
        sleep(100)
        fade()
        sleep(100)
