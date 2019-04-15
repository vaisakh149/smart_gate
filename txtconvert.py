import os
import tempfile
import subprocess
import time
import pandas as pd
import cv2
import csv
def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()

    os.remove(temp.name + '.txt')
    os.remove(temp.name)

    return contents

str = ocr('/home/esg/Downloads/robin_Vehicle-Number-Plate-Reading-master/result.jpg')
print(str)
raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
        'v_number': [str]}

row = [time.asctime( time.localtime(time.time()) ), str]

with open('data2.csv', 'a') as csvFile:
      writer = csv.writer(csvFile)
      writer.writerow(row)

csvFile.close()

