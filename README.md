# Overview
This is a very simple timelapse script meant to be run on a Raspberry Pi with an Arducam. For more information on how to set up an Arducam for the Raspberry Pi, check [this repository](https://github.com/simonjonsson87/TensorFlowPi.git).

The idea is that you just need to connect power to the Raspberry Pi to start the timelapse capture.

Parameters are configured in the script itself.

The script can be configured to only capture at certain times of day.

`startup.sh` is the script that is run from `crontab` to start on reboot. More details are below.

# A Few Practical Notes

Check how much space is available on the drive in Raspbian:
```
df -Bm
```

To set up the script to run when the Raspberry Pi starts, type `crontab -e` and add a line like:
```
@reboot /home/pi/RPi_Timelapse/startup.sh >> /home/pi/startup-output.log 2>&1
```