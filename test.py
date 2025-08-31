import os
from pathlib import Path
PROMPT = """If you can load the image 'FILENAME_PATH' and see what is there just output the word "'"True"'", Otherwise "'"Fa\
lse"'"""
rp=PROMPT.replace("FILENAME_PATH",os.path.abspath(str(Path(Path(__file__).parent.absolute(),"Scout.jpg"))))
print(rp)
