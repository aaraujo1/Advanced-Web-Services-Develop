# utilize gpio zero framework
from gpiozero import LED, Button

# utilize signal framework
from signal import pause

# where the LED get power
yellow_led = LED(18)

# where the button gets power
yellow_button = Button(15)


yellow_button.when_pressed = yellow_led.blink


#prevent program from ending immediatly
pause()

