# Program that runs the main code and utilizes code from other files
import os
from pathlib import Path
import argparser
import mkdirs


args = argparser.parse()

imgPath = os.path.join(str(Path.home()), "Pictures")
imgSortPath = mkdirs.loadDirs(imgPath, os.path.join(imgPath, "imgSort"))

print(os.listdir(args.Path))
