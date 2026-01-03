#! /bin/python3

import pickle
from PIL import Image as PILImage

def LoadOrder(orderFile):
	rf = open(orderFile, 'rb')
	order = pickle.load(rf)
	rf.close()
	return order

def MakeGif(order, fname, fps=60, width=1280, height=720, timelapseComment='TimeLapse', savePalette=False):
	images = [PILImage.open(sourceImage) for sourceImage in order]
	images[0].save(fname, save_all=True, append_images=images[1:], optimize=savePalette, duration=1000/fps, comment=timelapseComment, loop=0)

if __name__ == '__main__':
	name = 'Planter2024'
	outPath = '/home/justin.mcniel/Pictures/Timelapses/'
	inPath = outPath + name + '/'
	order = LoadOrder(inPath + 'order.pickle')
	MakeGif(order, outPath + name + '.gif')
