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
    
adrian =    [Image("00900:09090:09990:90909:90909"),
             Image("90909:09990:90909:00900:09090"),
             Image("90909:09990:99999:09990:90909")]
harris =    [Image("00000:00000:00000:00000:00700"),
             Image("00000:00000:00000:00700:00500"),
             Image("00000:00000:00900:00500:00300"),
             Image("00000:08880:08780:08880:00000"),
             Image("80808:07770:87678:07770:80808")]
maya =      [Image("97531:70000:50000:30000:10000"),
             Image("00000:0753:07000:05000:03000"),
             Image("00000:00000:00975:00700:00500"),
             Image("00000:00000:00000:00097:00070"),
             Image("00000:00000:00000:00000:00009")]
james =     [Image("99099:99999:99999:09990:00900"),
             Image("90909:09990:90909:09990:00900"),
             Image("00900:09090:90909:09990:00900"),
             Image("90909:00900:09090:00900:09090"),
             Image("00909:00990:09900:99090:90009"),
             Image("90909:09990:99999:09990:90909"),
             Image("09090:90909:09990:90909:09090"),
             Image("90909:09990:99999:09990:90909"),
             Image("90909:09090:90909:09090:90909")]
jacob =     [Image("00000:00000:00000:00000:00100"),
             Image("00000:00000:00000:00100:00200"),
             Image("00000:00000:00000:00200:00300"),
             Image("00000:00000:00000:00300:00400"),
             Image("00000:00000:00000:00400:00500"),
             Image("00000:00000:00000:00500:00600"),
             Image("00000:00000:00000:00600:00500"),
             Image("00000:00000:00000:00700:00400"),
             Image("00000:00000:00000:00800:00300"),
             Image("00000:00000:00000:00900:00000"),
             Image("00000:00000:00900:00900:00000"),
             Image("00000:00000:00900:00900:00000"),
             Image("00000:00000:00900:00800:00000"),
             Image("00000:00000:00900:00500:00000"),
             Image("00000:00500:00900:00000:00000"),
             Image("00000:00700:00900:00000:00000"),
             Image("00000:07970:00800:30003:00000"),
             Image("00900:04740:00500:40006:00000"),
             Image("00000:00700:00900:00500:00000"),
             Image("00900:00700:00900:00000:00000"),
             Image("00800:00700:00900:00000:00000"),
             Image("05050:50505:05050:00000:00000"),
             Image("05050:50505:05050:50050:00500"),
             Image("05050:50505:05050:50505:05050"),
             Image("05050:50505:05050:05050:50505"),
             Image("50505:05050:50505:50505:05050"),
             Image("05050:50505:05050:05050:50505"),
             Image("05050:50505:05050:50505:05050"),
             Image("05050:50505:05050:05050:50505"),
             Image("50505:05050:50505:50505:05050"),
             Image("05050:50505:05050:05050:50505"),
             Image("50505:05050:50505:50505:05050"),
             Image("05050:50505:05050:05050:50505")]
             
purple = (200, 0, 255)
dark_blue = (0, 0, 255)
green = (0, 255, 0)
orange = (255, 50, 0)
blue = (50, 50, 255)

fireworks = {
             'adrian': (adrian, dark_blue, 100, 20),
             'harris': (harris, orange, 400, 10),
             'maya': (maya, purple, 250, 0),
             'james': (james, blue, 500, 2),
             'jacob': (jacob, green, 150, 5)
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
