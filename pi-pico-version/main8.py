from neopixel import Neopixel
from machine import Pin
import time
import random
from pimoroni import Button, Buzzer                           # Change this line
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER

NEOPIXEL_DATA_PIN = 0
NEOPIXEL_LENGTH = 60

np = Neopixel(NEOPIXEL_LENGTH, 0, NEOPIXEL_DATA_PIN, "GRBW")

button_y = Button(15)
buzzer = Buzzer(5)                                    # Add this line
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
WHITE_PEN = display.create_pen(255, 255, 255)
BLACK_PEN = display.create_pen(0, 0, 0)
RED_PEN = display.create_pen(255, 63, 63)
display.set_font("sans")
display.set_thickness(5)

BURST_SIZE = 10

BLUE = (0, 0, 64, 0)
RED = (64, 0, 0, 0)
OFF = (0, 0, 0, 0)

FIREWORK_COLOURS = [ (255, 128, 128, 0), (128, 255, 128, 0), (128, 128, 255, 0)
                   , (255, 255, 128, 0), (255, 128, 255, 0), (128, 255, 255, 0)
                   ]
BASE_BUZZER_TONE = 40
BUZZER_INCREASE = 5
BUZZER_DECREASE = 2

def fade_all(first=0, last=NEOPIXEL_LENGTH, fade_by=0.9): # Change this line
    for i in range(first, last):
        fade(i, fade_by=fade_by)
    np.show()
        
def fade(n, fade_by=0.9):
    r, g, b, w = np.get_pixel(n)
    np.set_pixel(n, 
                 (int(r * fade_by), int(g * fade_by),
                  int(b * fade_by), int(w * fade_by)))

def reset():
    buzzer.set_tone(0)                      # Add this line

    display.set_pen(BLACK_PEN)
    display.clear()
    display.update()

    for n in range(NEOPIXEL_LENGTH):
        np.set_pixel(n, OFF)
    np.set_pixel(0, BLUE)
    np.show()

def shoot_firework():
    display.set_pen(BLACK_PEN)
    display.clear()
    display.set_pen(RED_PEN)
    display.text("Fire", 0, 100, scale=4)
    display.update()
    for pixel in range(NEOPIXEL_LENGTH - BURST_SIZE):
        np.set_pixel(pixel, RED)
        np.show()
        time.sleep(0.02)
        np.set_pixel(pixel, OFF)
        np.show()

def explode():    
    initial_colour = random.choice(FIREWORK_COLOURS) 
    
    buzzer_tone = BASE_BUZZER_TONE                    # Add this line
    buzzer.set_tone(buzzer_tone)        # Add this line
    
    for i in range(BURST_SIZE):
        np.set_pixel(NEOPIXEL_LENGTH - BURST_SIZE + i, initial_colour)
        np.set_pixel(NEOPIXEL_LENGTH - BURST_SIZE - i, initial_colour)
        fade_all( fade_by=0.9
                , first=(NEOPIXEL_LENGTH - BURST_SIZE - i)
                , last= (NEOPIXEL_LENGTH - BURST_SIZE + i)
                )

        buzzer_tone += BUZZER_INCREASE  # Add this line
        buzzer.set_tone(buzzer_tone)    # Add this line

    animation_delay = random.uniform(0.02, 0.1)
    animation_delay += random.uniform(0, 0.1)
    for _ in range(30):
        fade_all(first=(NEOPIXEL_LENGTH - 2 * BURST_SIZE),
                 fade_by=0.8)
        buzzer_tone -= BUZZER_DECREASE  # Add this line
        buzzer.set_tone(buzzer_tone)    # Add this line
        time.sleep(animation_delay)

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
        display.set_pen(BLACK_PEN) 
        display.clear()
        display.set_pen(WHITE_PEN)
        display.text(str(int(delay_timer / 10.0) + 1), 40, 100, scale=5)
        display.update()
        time.sleep(0.1)


