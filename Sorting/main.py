# Program that runs the main code and utilizes code from other files
import os
from pathlib import Path
from PIL import Image
import argparser
import mkdirs

file = open("output.txt", "w")
# args = argparser.parse()
impath = Path(os.path.join(Path.home(), "TEST"))

imgPath = os.path.join(str(Path.home()), "Pictures")
imgSortPath = mkdirs.loadDirs(imgPath, os.path.join(imgPath, "imgSort"))

pList = os.listdir(impath)
exifList = {}

for pic in pList:
    try:
        img = Image.open(os.path.join(impath, pic))
    except IOError:
        pass

    exif = img.getexif()

    exifList[str(pic)] = str(exif[36867])[0:10]
file.write(str(exifList))
file.close()
