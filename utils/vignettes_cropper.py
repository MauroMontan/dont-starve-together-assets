import os 
import sys
import time


# Mauro Montan
print('Vignette Cropper')

allowedImageExtension:list[str] = [".png",".jpg",".jpeg"]

imageSize = "1819x1023"

startPoint = "0+0"

targetFolder = sys.argv[1]



for file in os.listdir(targetFolder):
    
    filename,ext = os.path.splitext(file)
        
    for allowedExt in allowedImageExtension:
        if ext == allowedExt:
            os.system(f'convert {file} -crop {imageSize}+{startPoint} {file}')
            print(f"croping {filename} ..........")
            time.sleep(0.7)
            print("done\n")

    print('job finished')

