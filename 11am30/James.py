from microbit import *

for x in range(0, 5):
    for y in range(0, 5):
        display.set_pixel(x, y, 9)
        sleep(100)

while True:
    if button_a.was_pressed():
        poo = Image("99099:99999:99999:09990:00900")
        display.show(poo)
        sleep(1000)
        poo = Image("90909:09990:90909:09990:00900")
        display.show(poo)
        sleep(1000)
        poo = Image("00900:09090:90909:09990:00900")
        display.show(poo)
        sleep(1000)
        poo = Image("90909:00900:09090:00900:09090")
        display.show(poo)
        sleep(1000)
        poo = Image("00909:00990:09900:99090:90009")
        display.show(poo)
        sleep(1000)
        poo = Image("90909:09990:99999:09990:90909")
        display.show(poo)
        sleep(1000)
        poo = Image("09090:90909:09990:90909:09090")
        display.show(poo)
        sleep(1000)
        poo = Image("90909:09990:99999:09990:90909")
        display.show(poo)
        sleep(1000)
        poo = Image("90909:09090:90909:09090:90909")
        sleep(1000)
        poo = Image("00000:00000:00000:00000:00000")
        display.show(poo)
