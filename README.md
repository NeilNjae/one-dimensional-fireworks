In this session, you'll use a Raspberry Pi to program a Micro:bit, and the Microbit will control a NeoPixel strip and make it a one-dimensional firework.

# Connecting the Micro:bit and Neopixel strip
* Connect the black lead on the Neopixel strip to the GND hole on the Microbit.
* Connect the red lead on the Neopixel to the 3V hole on the Microbit.
* Connect the white lead on the Neopixel to the 0 hole on the Microbit.
* Use the USB cable to connect the Microbit to the Raspberry Pi

# Starting the Mu editor
Find the "Start" menu → Programming → mu
Once you've opened Mu, press the Mode button and press "BBC micro:bit"

# Program 1: launching the firework
Type this program into the Mu editor. It will do the animation for a firework launching.

Note that Python is really picky about 
* spacing and indentation
* upper and lower case letters
* round and square brackets
* colons at the end of some lines
* the difference between zero and oh, and one and ell.

> [Program 1](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks1.py)

When you've typed it in, press "Save" button to save your file then press the "Flash" button to put the program on the Microbit.

When you press the A button on the Microbit, you should see a little light shoot along the strip.

# Program 2: making the launch motion-sensitive
Pressing the button is OK, but let's make the firework launch if you shake the Microbit.

Make the changes indicated to your program. You don't need to type the '# Add this line' comments: that's just to show you what to do.

> [Program 2](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks2.py)

Again, save and flash the program. Now try shaking the Microbit and see if it launches a firework.

# Program 3: Exploding fireworks
Now to make the firework explode at the top!

> [Program 3](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks3.py)

Again, save and flash your program. You should now have explosions!

# Program 4
What you've got is OK, but let's add some animation to the explosion. Let's make it start small and rapidly grow, and then fade over a bit of time.

> [Program 4](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks4.py)

Again, save and flash the program. Cool animation!

# Program 5: different colour explosions
Always having the same colour explosion is a bit boring. Let's make every explosion a different colour.

> [Program 5](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks5.py)

Again, save and flash the program. Even cooler animation!

# Program 6: speeding up the animation
The animation's a bit slow. We can speed things up by only updating the pixels that change, rather than all of them.

> [Program 6](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks6.py)

# Program 7: Microbit display
The Microbit has a small display. Let's use that to show the firework is ready.

> [Program 7](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks7.py)

# Program 8: Radio control
The Micro:bit has a radio. Let's use that to make one firework (sometimes) set off another firework.

> [Program 8](https://github.com/NeilNjae/one-dimensional-fireworks/blob/master/fireworks8.py)