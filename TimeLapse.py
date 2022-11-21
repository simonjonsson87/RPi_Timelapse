from datetime import datetime, date, time
import os
import time
#import psutil
#disk = psutil.disk_usage('/')
#disk_free = disk.free / 2**30 # GiB

#PiLapse, originally written by The HatMan
#Note, all of the print lines can be commented out and are not necessary

active = False

#counts repeats of the while loop, can be commented out.
counter = 0

print('To escape loop, use Ctrl+C')
print()

INTERVAL = 708.0
FOLDER = '/home/pi/Pictures/'

timerstart = time.time()

com = 'raspistill -o current.jpg -q 100'
com = 'raspistill -o /home/pi/Pictures/current.jpg -q 100'
os.system('raspistill -o /home/pi/Pictures/current.jpg -q 100')# -w 1920 -h 1080')

print(time.time() - timerstart)

while active is True:
        
    # Check if the INTERVAL has passed yet.
	if (time.time() - timerstart > INTERVAL):
		#print(time.time() - timerstart)
		os.system('raspistill -o /home/pi/Pictures/current.jpg -q 100')
		#os.rename(FOLDER + 'current.jpg', FOLDER + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '.jpg')
		#print('renamed the file current.jpg')
		timerstart = time.time()

   #if current.jpg exists, rename it
	if (os.path.isfile('/home/pi/Pictures/current.jpg')):
		os.rename(FOLDER + 'current.jpg', FOLDER + datetime.now().strftime("%Y-%m-%d %H%M%S") + '.jpg')
	
	
	
	
	
	
	
	

    
