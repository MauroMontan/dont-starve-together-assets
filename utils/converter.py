import os
from pathlib import Path
import shutil
from rich.progress import Progress, SpinnerColumn, TextColumn


class Converter(object):
    
    def texToPng(self,targetFolder:Path,file:str,outFolder:Path,cleanWorkspace:bool):
        # used for docker
        rawTempOutFolder = "output"
        # used for file system
        absTempFolder = os.path.abspath(os.path.join(targetFolder,rawTempOutFolder))

    
        ktech  = """
        docker run --rm -u ktools -v "{targetFolder}:/data/" --platform linux/amd64 dstmodders/ktools ktech""".format(targetFolder=targetFolder)

        filename,ext = os.path.splitext(file)

        png_file_out = f"{rawTempOutFolder}/{filename}.png"



        if os.path.isdir(absTempFolder) == False:
            os.mkdir(absTempFolder)
    
        if ext == ".tex":
            if os.path.exists(os.path.join(outFolder,filename+".png")):
                print(f"🔵 {filename}.png alreay exist")
                
            else:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    transient=True,
                ) as progress:
                    progress.add_task(description=f"Processing {filename}...", total=None)
                    # Magic goes here :)
                    os.system(f'{ktech} --quiet {file} {png_file_out}')
                    if outFolder.is_dir() == False:
                        os.mkdir(outFolder)

                    
                    shutil.move(os.path.join(absTempFolder,f"{filename}.png"),outFolder)


                print(f"✅ {file} succesfully converted {'and removed!' if cleanWorkspace else '!'}")

            
                if cleanWorkspace:
                    to_remove_file = os.path.join(targetFolder,file)
                    os.remove(to_remove_file)
