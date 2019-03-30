from microbit import display, Image, sleep, pin0
import neopixel

np = neopixel.NeoPixel(pin0, 8)

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

annabel =   [Image("99999:99999:99999:99999"),
             Image("66779:55301:64735:76942:54375")]
olivia =    [Image("12345:23456:34567:45678:56789"),
             Image("23456:34567:45678:56789:45678"),
             Image("34567:45678:56789:45678:34567"),
             Image("99999:99999:99999:99999:99999"),
             Image("22222:55555:99999:55555:22222")]
frances =   [Image("00000:00000:00000:00000:00400"),
             Image("00000:00000:00000:00600:00200"),
             Image("00000:00000:00800:00400:00100"),
             Image("00000:00900:00600:00200:00000"),
             Image("98789:07670:00400:00100:00000"),
             Image("98789:87678:00200:00000:00000"),
             Image("98789:87678:90009:00000:00000")]
farhad =    [Image("90909:09990:99999:09990:90909"),
             Image("00900:09090:90909:09090:00900"),
             Image("90009:09090:90909:09090:90909")]
jem =       [Image("00000:00000:00000:00000:50000"),
             Image("00000:00000:00000:05000:00000"),
             Image("00000:00000:00500:00000:00000"),
             Image("00000:00000:00900:00000:00000"),
             Image("00000:09090:00900:09090:00000"),
             Image("90909:09090:90909:09090:90909"),
             Image("99999:99999:99999:99999:99999")]
daniel =    [Image("00000:00000:00000:00000:00500"),
             Image("00000:00000:00000:00500:00500"),
             Image("00000:00000:00600:00600:00000"),
             Image("00000:00700:00700:00000:00000"),
             Image("00000:00800:08880:00800:00000"),
             Image("00000:00800:08880:00800:00000"),
             Image("00800:00000:80808:00000:00800"),
             Image("00000:00000:00800:00000:00000"),
             Image("90009:07070:00000:07070:90009")]
oscar =     [Image("00090:90000:00900:00009:09000"),
             Image("00900:00000:90909:00000:00900"),
             Image("09000:00009:00900:90000:00090"),
             Image("00900:00000:90909:00000:00900"),
             Image("00090:90000:00900:00009:09000")]
abbylucy =  [Image('00000:00000:00000:00000:10000'),
             Image('00000:00000:00000:03000:10000'),
             Image('00000:00000:00600:03000:10000'),
             Image('00000:00090:00600:03000:10000'),
             Image('00606:00090:00606:03000:10000')]

purple = (200, 0, 255)
pink = (255, 0, 150)
dark_blue = (0, 0, 255)
green = (0, 255, 0)
orange = (255, 50, 0)
yellow = (255, 255, 0)
blue = (50, 50, 255)

fireworks = {
             'annabel': (annabel, purple, 100, 20),
             'olivia': (olivia, pink, 500, 20),
             'frances': (frances, dark_blue, 100, 20),
             'farhad': (farhad, purple, 1000, 20),
             'jem': (jem, green, 200, 10),
             'daniel': (daniel, orange, 100, 20),
             'oscar': (oscar, yellow, 100, 5),
             'abbylucy': (abbylucy, blue, 100, 10)
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
