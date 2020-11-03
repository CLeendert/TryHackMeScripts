import os
import zipfile
import time

with zipfile.ZipFile("final-final-compressed.zip", "r") as zip_ref:
    zip_ref.extractall('final-final-compressed')
    listOfFiles = os.listdir("final-final-compressed")
    for l in listOfFiles:
        if l.endswith(".zip"):
            with zipfile.ZipFile("final-final-compressed/"+l, "r") as zip_2:
                zip_2.extractall("final-final-compressed")
                os.remove("final-final-compressed/"+l)
