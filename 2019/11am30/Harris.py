from microbit import *

firework1 = (Image("00000:00000:00000:00000:00700"))
firework2 = (Image("00000:00000:00000:00700:00500"))
firework3 = (Image("00000:00000:00900:00500:00300"))
firework4 = (Image("00000:08880:08780:08880:00000"))
firework5 = (Image("80808:07770:87678:07770:80808"))
firework6 = (Image("60606:04440:64346:04440:60606"))
firework7 = (Image("30303:02220:32123:02220:30303"))
firework8 = (Image("20202:01110:21012:01110:20202"))
firework9 = (Image("10101:00000:10001:00000:10101"))
firework10 = (Image("00000:00000:00000:00000:00000"))
firework13 = (Image("90009:00000:00000:00000:90009"))
firework14 = (Image("59095:99099:00000:99099:59095"))
firework15 = (Image("35953:55955:99999:55955:35953"))
firework16 = (Image("00000:00000:00900:00000:00000"))

firework11 = [firework10,firework9,firework8,firework7,firework6,firework5,firework4,firework3,firework2,firework1,firework10,]
firework = [firework1,firework2,firework3,firework4,firework5,firework6,firework7,firework8,firework9,firework10,]
firework12 = [firework13,firework14,firework15,firework16,firework4,firework5,firework6,firework7,firework8,firework9,firework10,]

while True:
    if button_a.was_pressed():
        display.show(firework)
        display.show(firework11)
    if button_b.was_pressed():
        display.show(firework12)
