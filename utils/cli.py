#!/usr/bin/python3
import os
import typer
from pathlib import Path
from converter import Converter
import shutil

app = typer.Typer()

cv = Converter()

@app.command()
def converter(path:Path,output_folder:Path):
    cleanWorkspace:bool = typer.confirm("Clean workspace at finish (.tex files will be removed from workspace)")

    abspath = path.absolute()
    abs_outpath = output_folder.absolute()

    for file in os.listdir(abspath):
        cv.texToPng(path,file,abs_outpath,cleanWorkspace)
    
    shutil.rmtree(os.path.join(abspath,"output"))

    typer.echo("✨ Images are available here: "+ typer.style(abs_outpath,fg=typer.colors.BRIGHT_GREEN))


if __name__ == "__main__":
    app()
