import os 
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

imageSize = "478x694"  

startPoint = "30+30"

# convert wendy_sandbox.png -crop 478x694+30+30 wndy.png

for file in os.listdir():
    
    filename,ext = os.path.splitext(file)
        
    for allowedExt in allowedImageExtension:
        if ext == allowedExt:
            os.system(f'convert {file} -crop {imageSize}+{startPoint} {filename}-cropped{ext}') 
            print(f"croping {filename} ..........")
            time.sleep(0.7)
            print("done\n")

