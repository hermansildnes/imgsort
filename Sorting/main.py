# Program that runs the main code and utilizes code from other files
import os
from pathlib import Path
from PIL import Image
import shutil
import argparser
import mkdirs
import exifhandler
from sort import sort

args = argparser.parse()
if args.path:
    imgPath = Path(args.path)
else:
    imgPath = Path(os.path.join(Path.home(), "TEST"))

imgSortPath = mkdirs.loadDirs(
    imgPath, os.path.join(Path.home(), "Pictures", "imgSort")
)


exifList = exifhandler.createExifList(os.listdir(imgPath), imgPath)
sort(exifList, imgPath, imgSortPath)
