
import os, datetime, time, shutil, subprocess
import cv2, Arducam

start_hour = 4 # The time of day when capture will start. E.g. 4 will start capture at 04:00 in the morning
end_hour = 23 # Same as above for when the capture stops. 
INTERVAL = 2*60 # interval between images in seconds.
TARGET_FOLDER = '/home/pi/time-lapse/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + '/'
FOLDER_current = '/home/pi/time-lapse/'

cam = Arducam.Arducam()


isExist = os.path.exists(TARGET_FOLDER)
if not isExist:
   os.makedirs(TARGET_FOLDER)

timerstart = 0
active = True
while active is True:
        
	start = datetime.time(hour=start_hour, minute=0, second=0)
	end = datetime.time(hour=end_hour, minute=0, second=0)	
	current = datetime.datetime.now().time()
	print(current)
	if current > start and current < end:

		# Check if the INTERVAL has passed yet.
		if (time.time() - timerstart > INTERVAL):
			print('interval')
			image = cam.getFrame()
			cv2.imwrite(TARGET_FOLDER + 'current.jpg', image)
			timerstart = time.time()

		if (os.path.isfile(TARGET_FOLDER + 'current.jpg')):
			print('isfile')
			shutil.copyfile(TARGET_FOLDER + 'current.jpg', FOLDER_current + 'current.jpg')
			os.rename(TARGET_FOLDER + 'current.jpg', TARGET_FOLDER + datetime.datetime.now().strftime("%Y-%m-%d %H%M%S") + '.jpg')

	time.sleep(20)		
	
	
	
	
	
	
	
	

    
