# Functions for creating directories if they dont exsist, or if a new person is added
import os
from pathlib import Path
import time


def loadDirs(imgPath, imgSortPath):
    if not Path(imgPath).exists():
        print("\nPictures folder doesn´t exsist!")
        print("Creating Pictures folder...")
        os.mkdir(imgPath)

    if not Path(imgSortPath).exists():
        print("Creating imgSort folder...")
        os.mkdir(imgSortPath)

    return Path(imgSortPath)
