"""spotlight.py: This script helps you to get the windows spotlight wallpapers"""

import os
import shutil
from pathlib import Path
try:
    from PIL import Image
except:
    os.system("pip install Pillow")
    from PIL import Image

user_path = os.path.expanduser('~')
drive_letter = user_path[:2]

#this is the source path of windows spotlight images 
source_dir = f'{user_path}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
destination_dir = f'{user_path}/Pictures/Windows_Spotlight_Images'
portrait = f'{destination_dir}/Portrait'
landscape = f'{destination_dir}/Landscape'
Horizontal = (1920, 1080)
Vertical = (1080, 1920)

if os.path.exists(destination_dir) == False:
    os.mkdir(destination_dir)

if os.path.exists(portrait) == False:
    os.mkdir(portrait)

if os.path.exists(landscape) == False:
    os.mkdir(landscape)

lst = os.listdir(source_dir)   
        
assets = []

for files in lst:
    location = os.path.join(source_dir, files)
    size = os.path.getsize(location)
    if size > 143360:
        assets.append(files)

for f in assets:
    if os.path.exists(destination_dir+'/'+f+'.jpg') == False and os.path.exists(portrait+'/'+f+'.jpg') == False and os.path.exists(landscape+'/'+f+'.jpg') == False:
        shutil.copy(src=source_dir+f, dst=destination_dir)

def rename(img):
    p = Path(destination_dir+'/'+img)
    p.rename(p.with_suffix('.jpg'))

for f in assets:
    if os.path.exists(destination_dir+'/'+f+'.jpg') == False  and os.path.exists(portrait+'/'+f+'.jpg') == False and os.path.exists(landscape+'/'+f+'.jpg') == False:
        rename(f)
        # print(f)

def orientation(pic):
    image = Image.open(pic)
    if image.size == Horizontal:
        return 'landscape'
    elif image.size == Vertical:
        return 'portrait'

list_2 = os.listdir(destination_dir)

for file in list_2:
    if '.jpg' in file:
        if os.path.exists(portrait+'/'+file) == False and os.path.exists(landscape+'/'+file) == False:
            if orientation(destination_dir+'/'+file) == 'landscape':
                shutil.move(destination_dir+'/'+file, landscape)
            elif orientation(destination_dir+'/'+file) == 'portrait':
                shutil.move(destination_dir+'/'+file, portrait)

os.system(f'start {os.path.realpath(destination_dir)}')
