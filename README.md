# Overview
This is a very simple timelapse script which is meant to be ran on a Raspberry Pi and an Arducam. For more info on how to setup an Arducam for the Raspberry Pi, check [this repository](https://github.com/simonjonsson87/TensorFlowPi.git). 

The idea is that you just have to connect power to the Raspberry to start the timelapse capture. 

Parameters are configured in the script itself.

The script can be configure to only capture at certain times of day.

# Shout out
This code was inspired by PiLapse by The HatMan.

# A few practical notes

Check how much space on drive on Raspbian:
```
df -Bm
```

To setup the script to run when the raspberry starts, type ```crontab -e``` and add a line like:
```
@reboot /home/pi/RPi_Timelapse/startup.sh >> /home/pi/startup-output.log 2>&1
```