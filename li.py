import re
import glob, os
from PIL import Image

licenseDict = {}
charDict = {}
storeDict = '../chars/'
path = 'dataset/license_5/'

def parsingTxtFile(path):
    os.chdir(path)
    for file in glob.glob("*.txt"):
        if file != "classes.txt":
            lines = read_file(file)
            list = []
            for line in lines:
                list.append(line.split(" "))
            fName = os.path.splitext(file)[0] + '.jpg'
            licenseDict[fName] = list
        elif file == "classes.txt":
            lines = read_file(file)
            i = 0
            for line in lines:
                dataLine = line.split(" ")
                charDict[i] = dataLine[0].rstrip("\n")
                i = i + 1
    # print(charDict)

def read_file(file):
    with open(file, 'rt') as fd:
        lines = fd.readlines()
    return lines

def delete_file_in_folder(folder):
    if(os.path.isdir(folder)):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

def preProcess():
    listCharsReady = []
   
    for key in licenseDict:
        #os.chdir(path)
        # print(key)
        chars = licenseDict[key]
        imgPath = key
        img = Image.open(imgPath)
        dw, dh = img.size
        # print(chars)
        for char in chars:
            dirChar = storeDict + charDict[int(char[0])]
            # print(dirChar)
            if char[0] not in listCharsReady:
                # delete all exist files in the character folder
                delete_file_in_folder(dirChar)
                listCharsReady.append(char[0])
                # print(listCharsReady)
            dataCoordinate = char[1:]
            # print(dataCoordinate)
            x, y, w, h = map(float, dataCoordinate)
            left = int((x-w / 2) * dw)
            right = int((x + w / 2) * dw)
            top = int((y - h / 2) * dh)
            bottom = int((y + h / 2) * dh)
            if left < 0:
                l = 0
            if right > dw - 1:
                right = dw - 1
            if top < 0:
                top = 0
            if bottom > dh - 1:
                bottom = dh - 1
            # Crop license image
            cropImg = img.crop((left,top,right,bottom))
            if not os.path.exists(dirChar):
                os.makedirs(dirChar)
            numFileChar = len(os.listdir(dirChar)) + 1
            imgPathSave = dirChar +'/'+ charDict[int(char[0])]+"_"+str(numFileChar)+".jpg"
            cropImg.save(imgPathSave, 'JPEG')
        # print(listCharsReady)

if __name__ == "__main__":
    parsingTxtFile(path)
    preProcess()