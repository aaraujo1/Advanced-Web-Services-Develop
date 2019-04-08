# utilize gpio zero framework
from gpiozero import LED, Button

# utilize signal framework
from signal import pause

# where the LED get power
yellow_led = LED(14)
green_led = LED(17)
# where the button gets power
yellow_button = Button(15)
green_button = Button(18)

yellow_button.when_pressed = yellow_led.toggle
green_button.when_pressed = green_led.on
green_button.when_released = green_led.off

#prevent program from ending immediatly
pause()

