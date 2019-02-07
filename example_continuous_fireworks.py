from microbit import *
import SkyFawkes as sf
from random import choice

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

start11 = Image('00000:00000:00000:00000:00005')
start21 = Image('00000:00000:00000:00050:00003')
start31 = Image('00000:00000:00900:00030:00001')
start41 = Image('00000:09090:09790:09090:00000')
start51 = Image('90009:07070:07570:07070:90009')

start12 = Image('00000:00000:00000:00000:50000')
start22 = Image('00000:00000:00000:05000:30000')
start32 = Image('00000:00000:00900:03000:10000')
start42 = Image('00000:09900:00790:01090:00000')
start52 = Image('09900:97790:00579:00079:00009')

firework1 = [start11, start21, start31, start41, start51]
firework2 = [start12, start22, start32, start42, start52]

fireworks = [firework1, firework2]
colours = ["red", "green", "blue", "orange", "bluepurple", "redpurple", "pink",
           "yellow", "bluegreen", "greenblue", "white", "yellowgreen"]

def fade():
    for x in range(0, 5):
        for y in range(0, 5):
            value = display.get_pixel(x, y)
            if value > 0:
                display.set_pixel(x, y, value-1)

while True:
    lights = sf.colour(choice(colours))
    sf.turn_on(lights)
    display.show(choice(fireworks))
    for i in range(0, 9):
        fade()
        lights = sf.fade(lights)
        sf.turn_on(lights)
        sleep(400)
