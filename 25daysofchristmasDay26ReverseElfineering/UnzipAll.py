import os
import zipfile
import time

with zipfile.ZipFile("files.zip", "r") as zip_ref:
    zip_ref.extractall('files')
    listOfFiles = os.listdir("files")
    for l in listOfFiles:
        if l.endswith(".zip"):
            with zipfile.ZipFile("files/"+l, "r") as zip_2:
                zip_2.extractall("files")
                os.remove("files/"+l)
