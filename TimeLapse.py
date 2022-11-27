
import os, datetime, time, shutil
#import psutil
#disk = psutil.disk_usage('/')
#disk_free = disk.free / 2**30 # GiB

#PiLapse, originally written by The HatMan
#Note, all of the print lines can be commented out and are not necessary

start_hour = 4
end_hour = 16
INTERVAL = 5*60
FOLDER = '/home/pi/time-lapse/images/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + '/'
FOLDER_current = '/home/pi/time-lapse/images/'

isExist = os.path.exists(FOLDER)
if not isExist:
   os.makedirs(FOLDER)


timerstart = 0
active = True
while active is True:
        
	start = datetime.time(hour=start_hour, minute=0, second=0)
	end = datetime.time(hour=end_hour, minute=0, second=0)	
	current = datetime.datetime.now().time()
	if current > start and current < end:
		print('in loop')
		print(time.time() - timerstart)

		# Check if the INTERVAL has passed yet.
		if (time.time() - timerstart > INTERVAL):
			print('interval')
			os.system('raspistill -o ' + FOLDER + 'current.jpg -q 100')
			timerstart = time.time()

		if (os.path.isfile(FOLDER + 'current.jpg')):
			print('isfile')
			shutil.copyfile(FOLDER + 'current.jpg', FOLDER_current + 'current.jpg')
			os.rename(FOLDER + 'current.jpg', FOLDER + datetime.datetime.now().strftime("%Y-%m-%d %H%M%S") + '.jpg')

	time.sleep(2.5*60)		
	
	
	
	
	
	
	
	

    
