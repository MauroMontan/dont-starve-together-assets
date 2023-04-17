import os 
import sys
import time

allowedImageExtensions:list[str] = [".tex"]

targetFolder:str = sys.argv[1]

outputFolder:str = sys.argv[2]

ktech  = """
docker run --platform linux/amd64 --user='ktools' \
    --mount src='{targetFolder}',target='/data/',type=bind \
    dstmodders/ktools \
    ktech  """.format(targetFolder=targetFolder)



def converter():
    for file in os.listdir(targetFolder):
        filename, ext = os.path.splitext(file)


        for allowedExt in allowedImageExtensions:
            if ext == allowedExt:
                os.system(f'{ktech} {file} {outputFolder}/{filename}.png') 
                print(f"converting {filename} ....")
                time.sleep(0.7)


converter()
