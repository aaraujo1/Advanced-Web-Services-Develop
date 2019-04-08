# utilize gpio zero framework
from gpiozero import LED, Button

# utilize signal framework
from signal import pause

# where the LED get power
led = LED(14)
# where the button gets power
button = Button(15)

button.when_pressed = led.toggle

#prevent program from ending immediatly
pause()

