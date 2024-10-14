from neopixel import Neopixel
from machine import Pin
import time
import random                         # Add this line
from pimoroni import Button

NEOPIXEL_DATA_PIN = 0
NEOPIXEL_LENGTH = 60

np = Neopixel(NEOPIXEL_LENGTH, 0, NEOPIXEL_DATA_PIN, "GRBW")
button_y = Button(15)

BURST_SIZE = 10

BLUE = (0, 0, 64, 0)
RED = (64, 0, 0, 0)
OFF = (0, 0, 0, 0)

#########################################
# Add these functions
def fade_all(fade_by=0.9):
    for i in range(NEOPIXEL_LENGTH):
        fade(i, fade_by=fade_by)
    np.show()
        
def fade(n, fade_by=0.9):
    r, g, b, w = np.get_pixel(n)
    np.set_pixel(n, 
                 (int(r * fade_by), int(g * fade_by),
                  int(b * fade_by), int(w * fade_by)))
# End of functions to add
#########################################

def reset():
    for n in range(NEOPIXEL_LENGTH):
        np.set_pixel(n, OFF)
    np.set_pixel(0, BLUE)
    np.show()

def shoot_firework():
    for pixel in range(NEOPIXEL_LENGTH - BURST_SIZE):
        np.set_pixel(pixel, RED)
        np.show()
        time.sleep(0.02)
        np.set_pixel(pixel, OFF)
        np.show()

def explode():    
    initial_colour = (255, 128, 128, 0)
        
    for i in range(BURST_SIZE):
        np.set_pixel(NEOPIXEL_LENGTH - BURST_SIZE + i, initial_colour)
        np.set_pixel(NEOPIXEL_LENGTH - BURST_SIZE - i, initial_colour)
    # np.show()           # Remove this line
    # time.sleep(5)       # Remove this line
    for _ in range(30):   # Add this line
        fade_all()        # Add this line

reset()

delay_timer = 100

while True:
    if button_y.raw() or delay_timer <= 0:
        # set off a firework
        shoot_firework()
        explode() 
        reset()
        delay_timer = random.randint(50, 100) 
    else:
        delay_timer -= 1
        time.sleep(0.1)


