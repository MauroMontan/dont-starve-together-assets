#!/usr/bin/python3
# @MauroMontan
import os 
import sys
import time



# WARNING: This script only works with .text files 
allowedImageExtensions:list[str] = [".tex"]


#This is the folder where all your .tex files live :D
targetFolder:str = sys.argv[1]

#This s the name of your output folder

outputFolder:str = "output"

# This is the ktech command running from docker container 
ktech  = """
 docker run --rm -u ktools -v "{targetFolder}:/data/" --platform linux/amd64 dstmodders/ktools ktech""".format(targetFolder=targetFolder)



#This function creates output folder inside target folder
def outputFolderHandler(targetFolder:str):

    inner_paths:list[str] = os.listdir()
    if inner_paths.__contains__(outputFolder) == False: 
        output_path = os.path.join(targetFolder,"output")

        os.mkdir(output_path)

        print("content has been generated in: {output_path}".format(output_path=output_path))
    else: 
        print("output folder already exists")




def converter():

    outputFolderHandler(targetFolder)
    for file in os.listdir(targetFolder):
        filename, ext = os.path.splitext(file)


        for allowedExt in allowedImageExtensions:
            if ext == allowedExt:
                os.system(f'{ktech} {file} {outputFolder}/{filename}.png') 
                print(f"converting {filename} ....")
                time.sleep(0.7)



converter()

