from microbit import *

for x in range (1,5):
    firework=Image("97531:70000:50000:30000:10000")
    display.show(firework)
    sleep(500/x)
    firework=Image("00000:0753:07000:05000:03000")
    display.show(firework)
    sleep(500/x)
    firework=Image("00000:00000:00975:00700:00500")
    display.show(firework)
    sleep(500/x)
    firework=Image("00000:00000:00000:00097:00070")
    display.show(firework)
    sleep(500/x)
    firework=Image("00000:00000:00000:00000:00009")
    display.show(firework)
    sleep(500/x)
