from microbit import display, Image, sleep, pin1
import neopixel

np = neopixel.NeoPixel(pin1, 8)

def fade(time):
    for x in range(0, 5):
        for y in range(0, 5):
            b = display.get_pixel(x, y)
            if b > 0:
                display.set_pixel(x, y, b-1)
            sleep(time)

def turn_on(colour):
    for pixel in range(0, len(np)):
        np[pixel] = (colour[0], colour[1], colour[2])
    np.show()

def convert(integer):
    new = int(integer-3*(integer//10))
    integer = 0 if new < 5 else new
    return integer

def fade_np(colour):
    return (convert(colour[0]), convert(colour[1]), convert(colour[2]))

jake =      [Image("00000:00000:00000:00000:00900"),
             Image("00000:00000:00000:00900:00500"),
             Image("00000:00000:00900:00500:00000"),
             Image("55555:59595:55555:59595:55555"),
             Image("90009:06060:00100:06060:90009"),
             Image("80008:05050:00000:05050:80008"),
             Image("00000:70007:04040:00000:02020"),
             Image("00000:60006:03030:00000:00000"),
             Image("00000:50005:02020:00000:00000"),
             Image("00000:00000:40004:01010:00000"),
             Image("00000:00000:30003:00000:00000"),
             Image("00000:00000:20002:00000:00000"),
             Image("00000:00000:00000:10001:00000"),
             Image("00000:00000:00000:00000:00000")]
alex =      [Image("00000:00000:00900:00000:00000"),
             Image("00000:07070:00900:07070:00000"),
             Image("40004:07070:00900:07070:40004"),
             Image("00000:00000:00400:07000:90000"),
             Image("00000:00000:00400:07070:90009"),
             Image("90000:07000:00400:07070:90009"),
             Image("90009:07070:00400:07070:90009")]
anna =      [Image("00000:00000:00400:00000:00000"),
             Image("00000:00000:44444:00000:00000"),
             Image("00000:00400:44444:00400:00000"),
             Image("00500:00500:55555:00500:00500"),
             Image("00700:00770:77777:07700:00700"),
             Image("90909:09990:99999:09990:90909")]
charlie =   [Image("90909:09090:90909:09090:90909"),
             Image("09090:909090:09090:90909:09090"),
             Image("00000:009000:09990:00900:00000"),
             Image("90009:00000:00000:00000:90009"),
             Image("00800:00000:70707:00000:00800")]
dylan =     [Image("00000:00000:00000:00000:90000"),
             Image("00000:00000:00000:09000:00000"),
             Image("00000:00000:00900:00000:00000"),
             Image("00000:09090:00900:09090:00000"),
             Image("00900:09090:90909:09090:00900"),
             Image("90909:09090:90909:09090:90909")]
evie =      Image("90909:09990:99099:09990:90909")
louis =     [Image('00000:00000:00000:00000:90000'),
             Image('00000:00000:00000:09000:60000'),
             Image('00000:00000:00900:06000:30000'),
             Image('00000:00000:00600:03000:00000'),
             Image('00000:00000:00300:00000:00000'),
             Image('00000:09090:00900:09090:00000'),
             Image('90909:09090:90909:09090:90909'),
             Image('90909:09090:90009:09090:90909'),
             Image('90909:00000:90009:00000:90909'),
             Image('60606:00000:60006:00000:60606'),
             Image('30303:00000:30003:00000:30303'),
             Image('00000:00000:00000:00000:00000')]

purple = (200, 0, 255)
dark_blue = (0, 0, 255)
blue = (50, 50, 255)
turquoise = (0, 255, 255)
red = (255, 0, 0)

fireworks = {
             'jake': (jake, dark_blue, 200, 0),
             'alex': (alex, purple, 300, 20),
             'anna': (anna, turquoise, 100, 10),
             'charlie': (charlie, red, 500, 20),
             'dylan': (dylan, dark_blue, 200, 5),
             'evie': (evie, blue, 0, 20),
             'louis': (louis, blue, 300, 0)
            }

while True:
    for thing in fireworks:
        design, colour, wait1, wait2 = fireworks[thing]
        lights = colour
        turn_on(lights)
        display.show(design, delay=wait1)
        for i in range(0, 9):
            lights = fade_np(lights)
            turn_on(lights)
            fade(wait2)
