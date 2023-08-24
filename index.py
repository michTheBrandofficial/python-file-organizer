# File organizer app that takes the file extension of a file and knows where you put it in.
from pathlib import Path
from os import mkdir
from shutil import move

# read the current working directory using python
dir = input('Which directory do you wish to read? ') or '/test-fo'
path = Path(f".{ dir if dir[0] == '/' else f'/{dir}' }")

file_extension_mapping: dict[str , str] = {
  ".js": "/js" , 
  ".ts": "/ts" , 
  ".css": "/css" , 
  ".html": "/html" , 
}

if (path.iterdir()): 
  for x in path.iterdir():
    if x.is_file():
      # check is the extension exists in file_extension_mapping dict
      # if it does, make a new directory for it and add it to that directory if the dir exists
      # else, make the dir, then add it.
      fileInDir = Path(x)
      if (fileInDir.suffix in file_extension_mapping):
        extensionDir = Path(f'{path}{file_extension_mapping[fileInDir.suffix]}') 
        if (not extensionDir.exists()):
          mkdir(extensionDir)
          move(fileInDir , extensionDir)
        else:
          move(fileInDir , extensionDir)

    else: print("Can't work with directories yet")
