from gpiozero import MotionSensor, LED, Button
from time import sleep
from picamera import PiCamera
import datetime



class Modas:
	def __init__(self):
		# TODO: init PiCamera
		self.camera = PiCamera()
		# TODO: set camera resolution
		self.camera.resolution = (1024, 768)
		# init green, red LEDs
		self.green = LED(24)
		self.red = LED(23)
		# init button
		self.button = Button(8)
		# init PIR
		self.pir = MotionSensor(25)
		
		# when button  is released, toggle system arm / disarm
		self.button.when_released = self.toggle
		
		# system is disarmed by default
		self.armed = False
		self.disarm_system()
		
	def init_alert(self):
		self.green.off()
		self.red.blink(on_time=.25, off_time=.25, n=None, background=True)
		print("motion detected")
		# TODO: Take photo
		#camera.capture('/home/pi/Pictures/PISensor/image.jpg')
		self.snap_photo()
		# delay
		sleep(2)
		
	def reset(self):
		self.red.off()
		self.green.on()
		
	def toggle(self):
		self.armed = not self.armed
		if self.armed:
			self.arm_system()
		else:
			self.disarm_system()
			
	def arm_system(self):
		print("System armed in 3 seconds")
		self.red.off()
		# TODO: enable camera
		self.camera.start_preview()
		# 3 second delay
		self.green.blink(on_time=.25, off_time=.25, n=6, background=False)
		# enable PIR
		self.pir.when_motion = self.init_alert
		self.pir.when_no_motion = self.reset
		self.green.on()
		print("System armed")
		
	def disarm_system(self):
		# disable PIR
		self.pir.when_motion = None
		self.pir.when_no_motion = None
		# TODO: disable camera
		self.camera.stop_preview()
		self.red.on()
		self.green.off()
		print("System disarmed")
		
	def snap_photo(self):
		# TODO: set camera resolution
		#camera.resolution = (1024, 768)
		# TODO: enable camera
		#camera.start_preview()
		# TODO: Take photo
		now = datetime.datetime.now()
		date_time = now.strftime("%m-%d-%Y %H:%M:%S.%f")[:-3]
		self.camera.annotate_text = date_time
		self.camera.capture('/home/pi/Pictures/PISensor/image' + ' ' + date_time +'.jpg')
		print("Photo taken")
		# TODO: disable camera
		#camera.stop_preview()

m = Modas()

try:
	# program loop
    while True:
        sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
	if m.armed:
		m.disarm_system()
