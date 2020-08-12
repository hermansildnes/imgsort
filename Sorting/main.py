# Program that runs the main code and utilizes code from other files
import os
from pathlib import Path
import argparser
import mkdirs


args = argparser.parse()

IMGPATH = os.path.join(str(Path.home()), "Pictures")
IMGSORTPATH = os.path.join(IMGPATH, "imgSort")

IMGSORTPATH = mkdirs.loadDirs(IMGPATH, IMGSORTPATH)
