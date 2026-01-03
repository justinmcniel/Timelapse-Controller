#! /bin/sh

if [ ! -f /tmp/TimelapseRunning ]; then
	touch /tmp/TimelapseRunning
	(cd /home/justin.mcniel/Pictures/Timelapses; ./TimelapseShooter.py 1>> ./log.txt 2>>./error.txt) & exit 0
fi
