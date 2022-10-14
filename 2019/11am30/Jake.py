from microbit import *

fire1 = Image("00000:00000:00000:00000:00900")
fire2 = Image("00000:00000:00000:00900:00500")
fire3 = Image("00000:00000:00900:00500:00000")
fire4 = Image("55555:59595:55555:59595:55555")
fire5 = Image("90009:06060:00100:06060:90009")
fire6 = Image("80008:05050:00000:05050:80008")
fire7 = Image("00000:70007:04040:00000:02020")
fire8 = Image("00000:60006:03030:00000:00000")
fire9 = Image("00000:50005:02020:00000:00000")
fire10 = Image("00000:00000:40004:01010:00000")
fire11 = Image("00000:00000:30003:00000:00000")
fire12 = Image("00000:00000:20002:00000:00000")
fire13 = Image("00000:00000:00000:10001:00000")
fire14 = Image("00000:00000:00000:00000:00000")

#def fade():
#    for x in range(0,5):
#        for y in range(0,5):
#            br = display.get_pixel(y,x)
#            while br > 0:
#                display.set_pixel(y,x,br-1)
#                br = display.get_pixel(y,x)
#            sleep(100)


#def showpattern():
#    for x in range(0,5):
#        for y in range(0,5):
#            display.set_pixel(y,x,x+y+1)
#            sleep(100)
#    fade()



firework = [fire1, fire2, fire3, fire4, fire5, fire6, fire7, fire8, fire9, fire10, fire11, fire12, fire13, fire14]
display.show(firework, delay=200)

#while True:
#    if button_a.was_pressed():
#        display.show(firework, delay=200)
#    if button_b.was_pressed():
#        showpattern()
