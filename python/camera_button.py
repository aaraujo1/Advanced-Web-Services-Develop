from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()


camera.start_preview()
button.wait_for_press()
#add a delay
sleep(3)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()


#stop motion
'''
camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
'''
