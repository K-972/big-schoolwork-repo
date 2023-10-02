#A Halloween display needs a computer controlled light which will flicker.  Flicker the light for a random number of seconds between 1/10 and 1/100 of a second. You can use a pause function that takes as a parameter the number of milliseconds to pause the program. For example pause(1000) will pause the program for 1 second.  To turn the light on and off, set the value of light to HIGH for ON and LOW for OFF.  The control loop should run continuously.
import random
from random import randint

#on = high - off = low

light_status = 'low'

light_on_or_off = input('1 for on, 2 for off: ')

ran_time = random.uniform(0.1, 0.001)
print(ran_time)
def flicker(ran_time):
    pass