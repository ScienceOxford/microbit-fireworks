from microbit import *

fire1=(Image("00000:00000:00000:00000:60000"))
fire2=(Image("00000:00000:00000:06000:00000"))
fire3=(Image("00000:00000:00600:00000:00000"))
fire4=(Image("00650:00575:00056:00000:00000"))
fire=(Image("04654:04575:00456:00044:00000"))
fire5=(Image("02242:02454:02242:00222:00000"))
fire6=(Image("01111:11121:01111:11111:01111"))
fire7=(Image("00000:00010:00000:00000:00000"))
fire0=(Image("00000:00000:00000:00000:00000"))
fire8=(Image("00000:00000:00000:00000:00600"))
fire9=(Image("00000:00000:00000:00600:00000"))
fireA=(Image("00000:00000:00600:00000:00000"))
fireB=(Image("00000:00600:06760:00600:00000"))
fireC=(Image("00000:05650:06760:05650:00000"))
fireD=(Image("40004:05650:06660:05650:40004"))
#fireE=(Image("30003:04240:02520:04240:30003"))
#fireF=(Image("20002:02220:02320:02220:20002"))
#fireG=(Image("00000:00000:00100:00000:00000"))
firework=[fire1,fire2,fire3,fire4,fire,fire5,fire6,fire7,fire0,fire8,fire9,fireA,fireB,fireC,fireD]

display.show(firework,delay=300)


def fade():
    for x in range(0,5):
        for y in range(0,5):
            #display.set_pixel(y, x, 9)
            br=display.get_pixel(x, y)
            if br>0:
                display.set_pixel(x, y, br-1)


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
fade()
sleep(100)
fade()
sleep(100)
fade()
sleep(100)
fade()

firework=[fire1,fire2,fire3,fire4,fire,fire5,fire6,fire7,fire0,fire8,fire9,fireA,fireB,fireC,fireD]

while True:
    if button_a.was_pressed():
        display.show(firework,delay=300)
    fade()
    sleep(100)
