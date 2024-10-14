from neopixel import Neopixel
from machine import Pin
import time
import random                         # Add this line
from pimoroni import Button

NEOPIXEL_DATA_PIN = 0
NEOPIXEL_LENGTH = 60

BURST_SIZE = 10

np = Neopixel(NEOPIXEL_LENGTH, 0, NEOPIXEL_DATA_PIN, "GRBW")

button_y = Button(15)

BLUE = (0, 0, 64, 0)
RED = (64, 0, 0, 0)
OFF = (0, 0, 0, 0)

FIREWORK_COLOURS = [ (255, 128, 128, 0), (128, 255, 128, 0), (128, 128, 255, 0)
                   , (255, 255, 128, 0), (255, 128, 255, 0), (128, 255, 255, 0)
                   ]

def fade_all(first=0, last=NEOPIXEL_LENGTH, fade_by=0.9): # Change this line
    for i in range(NEOPIXEL_LENGTH):
        fade(i, fade_by=fade_by)
    np.show()
        
def fade(n, fade_by=0.9):
    r, g, b, w = np.get_pixel(n)
    np.set_pixel(n, 
                 (int(r * fade_by), int(g * fade_by),
                  int(b * fade_by), int(w * fade_by)))

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
    initial_colour = random.choice(FIREWORK_COLOURS) # Change this line
        
    for i in range(BURST_SIZE):
        np.set_pixel(NEOPIXEL_LENGTH - BURST_SIZE + i, initial_colour)
        np.set_pixel(NEOPIXEL_LENGTH - BURST_SIZE - i, initial_colour)
        fade_all( fade_by=0.9,               # Add this line
                , first=(NEOPIXEL_LENGTH - BURST_SIZE - i) # Add this line
                , last= (NEOPIXEL_LENGTH - BURST_SIZE + i) # Add this line
                )                           # Add this line

    for _ in range(30):
        fade_all(first=(NEOPIXEL_LENGTH - 2 * BURST_SIZE), # Change this line
                 fade_by=0.8 )                             # Change this line

reset()

delay_timer = 100 # Add this line

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


