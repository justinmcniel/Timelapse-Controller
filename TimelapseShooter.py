#! /bin/python3

TimelapseDir = '/home/justin.mcniel/Pictures/Timelapses/'
TimelapseName = 'Planter2024'
OutputDir = TimelapseDir + TimelapseName + '/'
SkipInitialDateCheck = True
width = 1280
height = 720
fps = 60

def Log(text):
	print(text)



def TakeAndSavePhoto(fname):
	Log('Taking Photo')
	for x in range(5): # 5 shots for auto exposure
		image = cam.get_image()
		time.sleep(1/5)

	Log('Displaying photo')
	catSurfaceObj = image
	windowSurfaceObj.blit(catSurfaceObj,(0,0))
	pygame.display.update()

	Log('Saving photo')
	pygame.image.save(windowSurfaceObj,fname)
	Log('Done Saving')

def StopTaking():
	cam.stop()
	pygame.quit()
	quit()

def PhotoDateStamps():
	currentDate = datetime.today().strftime('%d-%m-%Y')
	if SkipInitialDateCheck:
		currentDate = "00-00-0000"

	Log("Start Date: "+currentDate)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		newDate = datetime.today().strftime('%d-%m-%Y')

		if newDate != currentDate:
			currentDate = newDate
			Log("Date: "+currentDate)
			yield currentDate

		time.sleep(60) #in seconds

def AddFileToOrder(fname):
	readFile = open(OutputDir + 'order.pickle', 'rb')
	order = pickle.load(readFile)
	readFile.close()

	order.append(fname)

	writeFile = open(OutputDir + 'order.pickle', 'wb')
	pickle.dump(order, writeFile)
	writeFile.close()

	return order

if __name__ == '__main__':
	Log("=================================================")
	Log("Importing")
	import os
	import sys
	import time
	from datetime import datetime
	import pickle

	import TimelapseMaker

	import pygame
	from pygame.locals import *
	import pygame.camera

	Log("Initializing")
	pygame.init()
	pygame.camera.init()

	Log('Starting camera')
	cam = pygame.camera.Camera("/dev/video0",(width,height))
	cam.start()

	Log("Creating Window")
	windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
	pygame.display.set_caption('Camera')

	fileFormat = '.png'

	pastFirstLoop = False

	Log('Starting Timelapse Process')
	for dateString in PhotoDateStamps():
		fileName = OutputDir + dateString + fileFormat

		if not pastFirstLoop and SkipInitialDateCheck: #we would be overwriting a file
			newFname = fileName + '.' + datetime.now().strftime("%H:%M:%S") + '.orig'
			os.system('cp %s %s'%(fileName, newFname))
			rf = open(OutputDir + 'order.pickle', 'rb')
			currentOrder = pickle.load(rf)
			rf.close()

			modified = False

			for x in range(len(currentOrder)):
				if currentOrder[x] == fileName:
					currentOrder[x] = newFname
					modified = True

			if modified:
				wf = open(OutputDir + 'order.pickle', 'wb')
				pickle.dump(currentOrder, wf)
				wf.close()

		TakeAndSavePhoto(fileName)
		order = AddFileToOrder(fileName)
		TimelapseMaker.MakeGif(order, TimelapseDir + TimelapseName + '.gif', fps=fps, width=width, height=height, timelapseComment='Timelapse of %s'%TimelapseName, savePalette=False)

