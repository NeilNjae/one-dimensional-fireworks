from neopixel import Neopixel
from machine import Pin
import time
from pimoroni import Button

NEOPIXEL_DATA_PIN = 0
NEOPIXEL_LENGTH = 60

BURST_SIZE = 10
DISPLAY_ANIMATION_SPEED = 500 # Add this line

np = Neopixel(NEOPIXEL_LENGTH, 0, NEOPIXEL_DATA_PIN, "GRBW")

button_y = Button(15)

BLUE = (0, 0, 64, 0)
RED = (64, 0, 0, 0)
OFF = (0, 0, 0, 0)

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

reset()

while True:
    if button_y.raw():
        # set off a firework
        shoot_firework()
        reset()


