from microbit import *
import neopixel

NP_COUNT = 60
BURST_SIZE = 10

np = neopixel.NeoPixel(pin0, NP_COUNT)

BLUE = (0, 0, 64)
RED = (64, 0, 0)
OFF = (0, 0, 0)


def reset(pixels):
    for n in range(NP_COUNT):
        pixels[n] = OFF
    pixels[0] = BLUE
    np.show()
    
def shoot_firework(pixels):
    for pixel in range(NP_COUNT - BURST_SIZE):
        pixels[pixel] = RED
        pixels.show()
        sleep(20)
        pixels[pixel] = OFF
        pixels.show()
    

reset(np)
last_gesture = accelerometer.current_gesture() # Add this line

while True:
    gesture = accelerometer.current_gesture() # Add this line
    if gesture != last_gesture or button_a.is_pressed(): # Change this line
        # set off a firework
        shoot_firework(np)
        reset(np)
        last_gesture = gesture # Add this line