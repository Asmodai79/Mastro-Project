import os
import sys
from csvparser import readcsvFile

def sanitizeInput(file):
    if file.endswith('.csv'):
        return True
    else:
        return False

try:
    directory_name=sys.argv[1]
    print(directory_name)
except:
    print('Please pass directory_name')

fileList = os.listdir(directory_name)
for file in fileList:
    if sanitizeInput(file):
        print( " valid file: " + file)
        readcsvFile(file)
    else:
        print( " invalid file: " + file)





