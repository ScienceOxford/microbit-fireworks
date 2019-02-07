import neopixel
from microbit import pin1, sleep

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

# Library to control Neopixel fading, to be imported into the main fireworks code.

np = neopixel.NeoPixel(pin1, 12)

main = 150
sec = int(main//2)
none = 0

colours = {"red": (main, none, none), "green": (none, main, none),
           "blue": (none, none, main), "orange": (main, sec, none),
           "bluepurple": (sec, none, main), "redpurple": (main, none, sec),
           "pink": (main, sec, sec), "yellow": (main, main, none),
           "bluegreen": (none, sec, main), "greenblue": (none, main, sec),
           "white": (main, main, main), "yellowgreen": (sec, main, none)}

def colour(choice):
    if choice in colours:
        return colours.get(choice)
    else:
        return colours.get("white")

def convert(integer):
    new = int(integer-3*(integer//10))
    integer = 0 if new < 5 else new
    return integer

def fade(colour):
    return (convert(colour[0]), convert(colour[1]), convert(colour[2]))
    
def turn_on(colour):
    for pixel in range(0, len(np)):
        np[pixel] = (colour[0], colour[1], colour[2])
    np.show()
