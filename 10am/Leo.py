from microbit import *

firework = Image.SKULL


def ultramassiveblackhole():    
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            if br >0:
                display.set_pixel(x,y, br-1)
                sleep(50)


def ultramassiveblackhole2():    
    for x in range(0,5):
        for y in range(0,5):
            br=display.get_pixel(x,y)
            display.set_pixel(x,y, br+1)
            sleep(50)


while True:
    if button_a.was_pressed():
        display.show(firework)
    ultramassiveblackhole()                
    ultramassiveblackhole()        
    ultramassiveblackhole()         
    ultramassiveblackhole()
    ultramassiveblackhole() 
    ultramassiveblackhole() 
    ultramassiveblackhole() 
    ultramassiveblackhole() 
    ultramassiveblackhole()
    
    if button_b.was_pressed():
        display.show(firework)
    ultramassiveblackhole2()                
    ultramassiveblackhole2()        
    ultramassiveblackhole2()         
    ultramassiveblackhole2()
    ultramassiveblackhole2() 
    ultramassiveblackhole2() 
    ultramassiveblackhole2() 
    ultramassiveblackhole2() 
    ultramassiveblackhole2() 
