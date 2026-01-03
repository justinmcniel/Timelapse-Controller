This project was about creating a timelapse of a planter I had growing outside my front door.
It ran on a raspberry pi using raspbian and a USB webcam.
The output was set to sync with a private cloud so that it was backed up, and did not have to be manually retrieved.

starter.sh contains code to automatically start the project when the raspberry pi boots, that way I can simply plug it in and not worry about power outages or anything else like that.
TimelapseMaker.py contains code to compile the pre-captured still images into a gif for the timelapse. You could easily modify the code for other filetypes.
TimelapseShooter.py contains code controlling the camera and saving the photos. It uses pygame to take the photos, and pickle to save the list of photos that should be in the timelapse. It automattically takes a photo at a preset time, and if the time has passed without the photo being taken (ie. power outage), then it takes the photo when it can.

Most of this code is my own, but some small parts of it were copied from tutorials.
This code was never intended to be shared on someplace like GitHub (or I would have annotated the source of the tutorials), but I've had an increasing number of people asking to see it.
