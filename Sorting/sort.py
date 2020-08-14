import os
import shutil


def sort(exifList, imgpath, imgSortPath):
    for img in exifList:
        if not os.path.exists(
            os.path.join(imgSortPath, exifList[img]["Year"])
        ):
            os.mkdir(os.path.join(imgSortPath, exifList[img]["Year"]))

        shutil.copyfile(
            os.path.join(imgpath, img),
            os.path.join(imgSortPath, exifList[img]["Year"], img),
        )
