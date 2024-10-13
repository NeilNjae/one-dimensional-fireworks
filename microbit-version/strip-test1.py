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
    for pixel in range(NP_COUNT):
        # pixels[pixel] = (32, 0, 32)
        if pixel % 3 == 0:
            pixels[pixel] = (32, 32, 0)
        elif pixel % 3 == 2:
            pixels[pixel] = (32, 0, 32)
        else:
            pixels[pixel] = (0, 32, 32)
        pixels.show()
        sleep(20)
        
    #for pixel in range(NP_COUNT):
    #    pixels[pixel] = OFF
    #    pixels.show()
    

reset(np)

while True:
    if button_a.is_pressed():
        # set off a firework
        shoot_firework(np)
        # reset(np)
    if button_b.is_pressed():
        reset(np)