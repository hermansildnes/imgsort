from PIL import Image
import os


def createExifList(pList, imgpath):
    exifList = {}
    tempList = {}
    for pic in pList:
        try:
            img = Image.open(os.path.join(imgpath, pic))
        except IOError:
            pass

        exif = img.getexif()

        tempList[str(pic)] = str(exif[36867])[0:10]

    for temp in tempList:
        exifList[temp] = {
            "Year": tempList[temp][0:4],
            "Month": tempList[temp][5:7],
            "Date": tempList[temp][8:10],
        }

    return exifList
