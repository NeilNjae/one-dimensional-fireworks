In this session, you'll use a Raspberry Pi to control a NeoPixel strip and make it a one-dimensional firework.

# Connecting the NeoPixel to the Pi

1. Disconnect the Pi from the USB cable
2. Connect the _red_ lead on the Neopixel to the _3V3_ pin on the breakout board
3. Connect the _black_ lead on the Neopixel to the _GND_ pin on the breakout board
4. Connect the _white_ lead on the Neopixel to pin _0_ on the breakout board
5. Reconnect the USB cable

# Flash the Pimoroini firmware

Follow the [Pimoroni instructions](https://learn.pimoroni.com/article/getting-started-with-pico#installing-the-custom-firmware) . As of time of writing, I'm using [pico-v1.23.0-1-pimoroni-micropython.uf2](https://github.com/pimoroni/pimoroni-pico/releases)

# Starting the Thonny editor

Have it auto-detect the Pi.

# Installing the Neopixel library

Neopixels need a library to drive the Neopixels. I use "blaz-r"'s [pi_pico_neopixel](https://github.com/blaz-r/pi_pico_neopixel?tab=readme-ov-file) library. Download the `neopixels.py` file, open it in Thonny, then save it as `neopixels.py` on the Pi.

See the [library documentation](https://github.com/blaz-r/pi_pico_neopixel/wiki/Library-methods-documentation) for other things it can do.


# Program 1: launching the firework
Type this program into the Thonny editor. It will do the animation for a firework launching.

Note that Python is really picky about 
* spacing and indentation
* upper and lower case letters
* round and square brackets
* colons at the end of some lines
* the difference between zero and oh, and one and ell.

> [Program 1](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main1.py)

When you've typed it in, "Save As…" the file to `main.py` on the Pi Pico. Then press the "Run" button to put the program on the Pi Pico.

When you press the Y button on the Pico Explorer board, you should see a little light shoot along the strip.

# Program 2: making the launch automatic
Pressing the button is OK, but let's make the firework launch after a short delay.

Make the changes indicated to your program. You don't need to type the '# Add this line' comments: that's just to show you what to do.

> [Program 2](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main2.py)

Again, save the program on the Pi Pico as `main.py`. Now leave the button alone and see if it makes the firework launch by itself.

# Program 3: Exploding fireworks
Now to make the firework explode at the top!

> [Program 3](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main3.py)

Again, save and flash your program. You should now have explosions!

# Program 4
What you've got is OK, but let's add some animation to the explosion. Let's make it start small and rapidly grow, and then fade over a bit of time.

> [Program 4](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main4.py)

Again, save and flash the program. Cool animation!

# Program 5: different colour explosions
Always having the same colour explosion is a bit boring. Let's make every explosion a different colour.

> [Program 5](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main5.py)

Again, save and flash the program. Even cooler animation!

# Program 6: speeding up the animation
When real fireworks explode, the outer edge of the explosion is bright and the centre gets dimmer. Let's change the animation to do that. 

The animation's a bit slow. We can speed things up by only updating the pixels that change, rather than all of them. But when we do, the animation's too fast! 

We need to add an explicit delay in the "fading" loop so we can see the animation. Experiment with adjusting the value of `time.sleep`, and the number of fading steps, to have an animation that looks good. (But don't spend so long that you can't do the next steps.)

> [Program 6](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main6.py)

# Program 7: Explorer display
The Explorer has a small display. Let's use that to show a countdown.

> [Program 7](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main7.py)

# Program 8: Annoying sound
The Explorer has a small piezo-electric buzzer. We can use that to make an annoying sound when the firework goes off.

On the Explorer board, put a jumper between the "Audio" pin and GPIO pin 5.

> [Program 8](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/pi-pico-version/main8.py)