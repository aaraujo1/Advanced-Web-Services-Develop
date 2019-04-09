from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

#SOURCE: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8

#to rotate camera
#camera.rotation = 180

#camera transparency
#camera.start_preview(alpha=100)

#to turn on
#camera.start_preview()
#sleep(10)
#camera.stop_preview()

#take a photo
'''
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
'''

#take 5 photos
'''
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
'''

#take video
'''
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
'''

#configure camera
'''
#camera.resolution = (2592, 1944)
camera.resolution = (64, 64)
camera.framerate = 15
camera.start_preview()
sleep(5)
#camera.capture('/home/pi/Desktop/max.jpg')
camera.capture('/home/pi/Desktop/min.jpg')
camera.stop_preview()
'''

#annotate
'''
camera.start_preview()
camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()
'''

#adjust brightness
'''
camera.start_preview()
camera.brightness = 70
sleep(5)
camera.capture('/home/pi/Desktop/bright.jpg')
camera.stop_preview()
'''

#adjust brightness with a loop
'''
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()
'''

#adjust contrast with a loop
'''
camera.start_preview()
#adjust text size
camera.annotate_text_size = 50
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()
'''

#playing with color
'''
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()
'''

#color filters
'''
camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()
'''

#image effects
'''
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
camera.stop_preview()
'''

#auto white balance
'''
camera.start_preview()
camera.awb_mode = 'fluorescent'
sleep(5)
camera.capture('/home/pi/Desktop/sunlight.jpg')
camera.stop_preview()
'''

#camera exposure
camera.start_preview()
camera.exposure_mode = 'beach'
sleep(5)
camera.capture('/home/pi/Desktop/beach.jpg')
camera.stop_preview()




