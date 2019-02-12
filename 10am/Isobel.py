from microbit import *

firework=Image("00500:05050:50005:05050:00500")
#display.show(Image("00900:09090:90009:09090:00900"))
#sleep(100)
#display.show(Image("00000:00700:07070:00700:00000"))


def fade():
    for x in range(0,5):
        for y in range(0,5):
            #display.set_pixel(x,y,9)
            br=display.get_pixel(x,y)
            if br>0:
                display.set_pixel(x,y,br-1)
            sleep(1)


def brighten():
    for x in range(0,5):
        for y in range(0,5):
            #display.set_pixel(x,y,9)
            brd=display.get_pixel(x,y)
            if br<9:
                display.set_pixel(x,y,brd+1)
            sleep(1)


while True:
    if button_a.was_pressed():
        display.show(firework)
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
    
#while True:
    if button_b.was_pressed():
        display.show(Image("00100:01010:10001:01010:00100"))
    brighten() 
    sleep(100)
    brighten() 
    sleep(100)
    brighten() 
    sleep(100)
    brighten() 
    sleep(100)
    brighten() 
    sleep(100)
    brighten() 
    sleep(100)
    brighten() 
    sleep(100)
