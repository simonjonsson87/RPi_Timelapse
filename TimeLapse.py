from datetime import datetime, date, time
import os
import time, shutil
#import psutil
#disk = psutil.disk_usage('/')
#disk_free = disk.free / 2**30 # GiB

#PiLapse, originally written by The HatMan
#Note, all of the print lines can be commented out and are not necessary

start = time(hour=4, minute=0, second=0)
end = time(hour=16, minute=0, second=0)
INTERVAL = 3000
FOLDER = '/home/pi/time-lapse/images/' + datetime.now().strftime("%Y-%m-%d_%H%M%S")
FOLDER_current = '/home/pi/time-lapse/images/'



timerstart = time.time()
os.system('raspistill -o /home/pi/Pictures/current.jpg -q 100')# -w 1920 -h 1080')

active = True
while active is True:
        
	
	current = datetime.now().time()
	if current > start and current < end:

		# Check if the INTERVAL has passed yet.
		if (time.time() - timerstart > INTERVAL):
			os.system('raspistill -o ' + FOLDER + 'current.jpg -q 100')
			timerstart = time.time()

		if (os.path.isfile(FOLDER + 'current.jpg')):
			shutil.copyfile(FOLDER + 'current.jpg', FOLDER_current + 'current.jpg')
			os.rename(FOLDER + 'current.jpg', FOLDER + datetime.now().strftime("%Y-%m-%d %H%M%S") + '.jpg')

	time.sleep(1000)		
	
	
	
	
	
	
	
	

    
