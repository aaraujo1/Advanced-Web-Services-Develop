from picamera import PiCamera
from time import sleep
from gpiozero import Button
import datetime
from signal import pause

button = Button(17)
camera = PiCamera()


#i=0


'''
Create a Python program that will take a photo every time a button is pressed. 
The camera preview should be enabled for at least 2 seconds before the photo is taken.
The photos should never be overwritten. You will need to come up with a naming convention that will ensure that the name of each photo will be unique.
Add a timestamp to the actual photo that includes the precise date/time that the photo was taken.
Hint: you will want to look at the datetime Python framework
'''

#button.wait_for_press()

#define function
def take_photo():
	camera.start_preview()
	now = datetime.datetime.now()
	date_time = now.strftime("%m-%d-%Y %H:%M:%S.%f")[:-3]
	camera.annotate_text = date_time
	#i += 1
	#add a delay for at least 2 seconds before the photo is taken
	sleep(2)
	camera.capture('/home/pi/image' + str(i) + ' ' + date_time +'.jpg')
	camera.stop_preview()
	print('photo ' + str(i) + ' taken')

button.when_released = take_photo

pause()



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
