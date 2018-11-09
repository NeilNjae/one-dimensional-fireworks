from microbit import *
import neopixel

NP_COUNT = 60
BURST_SIZE = 10

np = neopixel.NeoPixel(pin0, NP_COUNT)

BLUE = (0, 0, 64)
RED = (64, 0, 0)
OFF = (0, 0, 0)


#########################################
# Add this function
def explode(pixels):    
    initial_colour = (255, 128, 128)
        
    for i in range(BURST_SIZE):
        pixels[NP_COUNT - BURST_SIZE + i] = initial_colour
        pixels[NP_COUNT - BURST_SIZE - i] = initial_colour
    pixels.show()
    time.sleep(0.5)
# End of function to add
#########################################

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
        explode(np) # Add this line
        reset(np)
        last_gesture = gesture
