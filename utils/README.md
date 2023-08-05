# tools for extracting and cropping game assets

This tool use [dstmodders/ktools](https://hub.docker.com/r/dstmodders/ktools#!), so you docker is required

## Requirements

- Docker installed
- Python3 interpreter

## Usage

its usage is as simple as run the below command in your terminal to convert any amount of .tex files to png.

```bash
./cli.py <WORKSPACE> <OUTPUTFOLDER>
```

- Wrokspace folder:

    The workspace folder is where your .tex files are ready to convert (I recommend using     workspace folder just for tex foles).

- Output folder:

    where your images will be saved (path will be echoed when finished).
    WARNING: if your output folder is in your workspace direcotry it can not be named "output"
