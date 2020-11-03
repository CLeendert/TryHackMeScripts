import os
import exiftool

files = os.listdir("/mnt/c/users/cleen/documents/github/tryhackme/25daysofchristmasDay16-FileConfusion/")

with exiftool.ExifTool() as et:
	metadata = et.get_metadata_batch(files)
	
for d in metadata: 
	if "XMP:Version" in d.keys():
		print("File Name: {} Version: {}".format(d["SourceFile"], d["XMP:Version"]))