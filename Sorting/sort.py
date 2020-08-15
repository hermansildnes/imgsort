import os
import shutil
import time


def sort(exifList, imgPath, imgSortPath):
    for img in exifList:
        if not os.path.exists(
            os.path.join(imgSortPath, exifList[img]["Year"])
        ):
            print('Creating folder "{0}"'.format(exifList[img]["Year"]))
            os.mkdir(os.path.join(imgSortPath, exifList[img]["Year"]))

        print(
            'Moving "{0}" to folder "{1}"'.format(img, exifList[img]["Year"])
        )
        shutil.copyfile(
            os.path.join(imgPath, img),
            os.path.join(imgSortPath, exifList[img]["Year"], img),
        )
        time.sleep(0.05)
