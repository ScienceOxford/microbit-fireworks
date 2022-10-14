from microbit import *

#firework = Image.HAPPY
firework_1 = Image("00000:"
                  "00000:"
                  "00900:"
                  "00000:"
                  "00000")

firework_2 = Image("00000:"
                  "30903:"
                  "09890:"
                  "30903:"
                  "00000")

firework_3 = Image("30703:"
                  "09790:"
                  "97679:"
                  "09790:"
                  "30903")

firework_4 = Image("00400:"
                  "04640:"
                  "46464:"
                  "04640:"
                  "00400")

firework_4 = Image("00000:"
                  "00100:"
                  "01210:"
                  "00100:"
                  "00000")

firework_5 = Image("00000:"
                  "00000:"
                  "00100:"
                  "00000:"
                  "00000")
                  
images = [firework_1,firework_2,firework_3,firework_4,firework_5 ]

n = 9
for i in range(n):
    for image in images:
        display.show(image)
        sleep(100)
