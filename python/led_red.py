# utilize gpio zero framework
from gpiozero import LED

# utilize signal framework
from signal import pause

# connect GPIO pin 14 to led
# led_blue is variable name
led_blue = LED(14)

# turn led "on"
led_blue.on()

#prevent program from ending immediatly
pause()

