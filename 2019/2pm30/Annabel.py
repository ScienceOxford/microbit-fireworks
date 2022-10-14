from microbit import *
import music

firework=Image("99999:99999:99999:99999")
firework2=Image("66779:55301:64735:76942:54375")
display.show(firework)
sleep(100) 
display.show(firework2)


def fade():
    for x in range(0,5):
      for y in range (0,5):
          br=display.get_pixel(x,y)
          if br> 0:
              display.set_pixel(x,y,br-1)
      sleep(100)


while True:
    if button_a.was_pressed():
        display.show(firework)
        music.play(music.ODE)
        
fade()
fade()
fade()
fade()
fade()
