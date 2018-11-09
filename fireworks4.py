from microbit import *
import neopixel

NP_COUNT = 60
BURST_SIZE = 10

np = neopixel.NeoPixel(pin0, NP_COUNT)

BLUE = (0, 0, 64)
RED = (64, 0, 0)
OFF = (0, 0, 0)

#########################################
# Add these functions
def fade_all(pixels, fade_by=0.9):
    for i in range(NP_COUNT):
        fade(pixels, i, fade_by=fade_by)
    pixels.show()
        
def fade(pixels, n, fade_by=0.9):
    r, g, b = pixels[n]
    pixels[n] = (int(r * fade_by), int(g * fade_by), int(b * fade_by))
# End of functions to add
#########################################

def explode(pixels):    
    initial_colour = (255, 128, 128)
            
    for i in range(BURST_SIZE):
        pixels[NP_COUNT - BURST_SIZE + i] = initial_colour
        pixels[NP_COUNT - BURST_SIZE - i] = initial_colour
        fade_all(pixels, fade_by=0.95) # Add this line
    # pixels.show() # Remove this line
    # time.sleep(0.5) # Remove this line

    for _ in range(30): # Add this line
        fade_all(pixels) # Add this line

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
last_gesture = accelerometer.current_gesture()

while True:
    gesture = accelerometer.current_gesture()
    if gesture != last_gesture or button_a.is_pressed():
        # set off a firework
        shoot_firework(np)
        explode(np)
        reset(np)
        last_gesture = gesture