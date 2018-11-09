from microbit import *
import neopixel
import random
import radio # Add this line

NP_COUNT = 60
BURST_SIZE = 10
DISPLAY_ANIMATION_SPEED = 500

np = neopixel.NeoPixel(pin0, NP_COUNT)

radio.on() # Add this line

BLUE = (0, 0, 64)
RED = (64, 0, 0)
OFF = (0, 0, 0)

# Add this block
FIREWORK_COLOURS = [ (255, 128, 128), (128, 255, 128), (128, 128, 255)
                   , (255, 255, 128), (255, 128, 255), (128, 255, 255)
                   ]

def fade_all(pixels, first=0, last=NP_COUNT, fade_by=0.9):
    for i in range(first, last):
        fade(pixels, i, fade_by=fade_by)
    pixels.show()
        
def fade(pixels, n, fade_by=0.9):
    r, g, b = pixels[n]
    pixels[n] = (int(r * fade_by), int(g * fade_by), int(b * fade_by))

def explode(pixels):    
    initial_colour = random.choice(FIREWORK_COLOURS)
            
    for i in range(BURST_SIZE):
        pixels[NP_COUNT - BURST_SIZE + i] = initial_colour
        pixels[NP_COUNT - BURST_SIZE - i] = initial_colour
        fade_all( pixels, fade_by=0.95
                , first=(NP_COUNT - BURST_SIZE - i)
                , last= (NP_COUNT - BURST_SIZE + 1)
                )

    for _ in range(30):
        fade_all(pixels,  first=(NP_COUNT - 2 * BURST_SIZE))

def reset(pixels):
    for n in range(NP_COUNT):
        pixels[n] = OFF
    pixels[0] = BLUE
    np.show()
    display.show(Image.DIAMOND) 

    
def shoot_firework(pixels):
    display.show(Image.ARROW_S)
    for pixel in range(NP_COUNT - BURST_SIZE):
        pixels[pixel] = RED
        pixels.show()
        sleep(20)
        pixels[pixel] = OFF
        pixels.show()
    

def all_firework():
    radio.send('fire') # Add this line
    shoot_firework(np)
    explode(np)
    reset(np)


reset(np)
display_timer = 0
radio_timer = 0
last_gesture = accelerometer.current_gesture()

while True:
    gesture = accelerometer.current_gesture() 
    if gesture != last_gesture or button_a.is_pressed():
        # set off a firework
        all_firework()
        last_gesture = gesture
    elif radio_timer > 0 and radio_timer == display_timer:
        all_firework()
        radio_timer = 0
        last_gesture = gesture
    else:
        # animate the waiting
        display_timer = (display_timer + 1) % DISPLAY_ANIMATION_SPEED
        if display_timer > (DISPLAY_ANIMATION_SPEED / 2):
            display.show(Image.DIAMOND_SMALL)
        else:
            display.show(Image.DIAMOND)
    received = radio.receive()
    if received == 'fire' and random.randrange(5) == 0:
        radio_timer = (display_timer + random.randint(50, 350)) % DISPLAY_ANIMATION_SPEED
