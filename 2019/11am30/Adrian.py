from microbit import *

firework=(Image("00900:09090:09990:90909:90909"))
sleep(100)
firework2=(Image("90909:09990:90909:00900:09090"))
display.show(firework2)
sleep(100)
firework3=(Image("90909:09990:99999:09990:90909"))
display.show(firework3)

for x in range(0,5):
    for y in range(0,5):
         br=display.get_pixel(x,y)
         if br>0:
                display.set_pixel(x,y,br-9)
         sleep(100)

display.show(firework)

for x in range(0,5):
    for y in range(0,5):
         br=display.get_pixel(x,y)
         if br>0:
                display.set_pixel(x,y,br-9)
         sleep(100)

display.show(firework2)

for x in range(0,5):
    for y in range(0,5):
         br=display.get_pixel(x,y)
         if br>0:
                display.set_pixel(x,y,br-9)
         sleep(100)

display.show(firework3)
