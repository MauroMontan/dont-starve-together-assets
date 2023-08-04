import os 
import sys
import time

print("""
                                                                                                                   
  ####  #####   ####  #####  # #    #  ####     # #    #   ##    ####  ######       #####  ####   ####  #      
 #    # #    # #    # #    # # ##   # #    #    # ##  ##  #  #  #    # #              #   #    # #    # #      
 #      #    # #    # #    # # # #  # #         # # ## # #    # #      #####          #   #    # #    # #      
 #      #####  #    # #####  # #  # # #  ###    # #    # ###### #  ### #              #   #    # #    # #      
 #    # #   #  #    # #      # #   ## #    #    # #    # #    # #    # #              #   #    # #    # #      
  ####  #    #  ####  #      # #    #  ####     # #    # #    #  ####  ######         #    ####   ####  ######
        """)

allowedImageExtension:list[str] = [".png",".jpg",".jpeg"]

imageSize = "511x624"  

startPoint = "0+45"

targetFolder = sys.argv[1]

# convert wendy_sandbox.png -crop 511x624+0+45 wndy.png

for file in os.listdir(targetFolder):

    print("filename: {file}".format(file=file))
    
    filename,ext = os.path.splitext(file)
        
    for allowedExt in allowedImageExtension:
        if ext == allowedExt:
            os.system(f'sudo convert {file} -crop {imageSize}+{startPoint} {file}') 
            print(f"croping {filename} ..........")
            time.sleep(0.2)
            print("done\n")

