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

isobel =    [Image("00100:01010:10001:01010:00100"),
             Image("00300:03030:30003:03030:00300"),
             Image("00500:05050:50005:05050:00500"),
             Image("00700:07070:70007:07070:00700"),
             Image("00900:09090:90009:09090:00900")]
oliver =    Image("05950:59995:59995:03930:01910")
toby =      [Image("00000:00000:00000:00000:60000"),
             Image("00000:00000:00000:06000:00000"),
             Image("00000:00000:00600:00000:00000"),
             Image("00650:00575:00056:00000:00000"),
             Image("04654:04575:00456:00044:00000"),
             Image("02242:02454:02242:00222:00000"),
             Image("01111:11121:01111:11111:01111"),
             Image("00000:00010:00000:00000:00000"),
             Image("00000:00000:00000:00000:00000"),
             Image("00000:00000:00000:00000:00600"),
             Image("00000:00000:00000:00600:00000"),
             Image("00000:00000:00600:00000:00000"),
             Image("00000:00600:06760:00600:00000"),
             Image("00000:05650:06760:05650:00000"),
             Image("40004:05650:06660:05650:40004")]
leo =       [Image("01110:10101:11111:01110:01110"),
             Image("03330:30303:33333:03330:03330"),
             Image("05550:50505:55555:05550:05550"),
             Image("07770:70707:77777:07770:07770"),
             Image("09990:90909:99999:09990:09990")]
zaniel =     Image("90009:09090:00900:09090:90009")

purple = (200, 0, 255)
dark_blue = (0, 0, 255)
blue = (50, 50, 255)
turquoise = (0, 255, 255)
red = (255, 0, 0)

fireworks = {
             'isobel': (isobel, turquoise, 100, 10),
             'oliver': (oliver, red, 0, 20),
             'toby': (toby, purple, 300, 2),
             'leo': (leo, dark_blue, 100, 20),
             'zaniel': (zaniel, blue, 0, 20)
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
