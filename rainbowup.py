import argparse
import os
import sys
import glob
# run python3 -m pip install --upgrade Pillow if you didn't install PIL already
from PIL import Image
RAINBOW_FILTER = 'filter.png'
RAINBOW_SMOOTH = 'filter_s.jpeg'

doc = """
This is a script created by Mt. Front to bulk apply rainbow filter to images.

On 7/7/2021, Chinese government banned all Wechat (largest Chinese social network) channels related to LGBT rights. 
This script is just a silent protest.

Find the source code at https://github.com/mfcndw/rainbowup

*** Warning: This script has only been tested on MacOS ***

Usage:
   `python3 rainbowup.py path [-a] [-s] [-f] [-h]`
"""

# parsing args
parser = argparse.ArgumentParser(description=doc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument(dest="path", help="The path of image or directory needs to be rainbowed up")
parser.add_argument('-a', '--alpha', type=int, action='store', default=130, help="The opacity of the filter, default to 130. range from 0 (not visible) - 255")
parser.add_argument('-s', '--smooth', action='store_true', default=False, help="Switch to a smooth rainbow filter. Default to false")
parser.add_argument('-f', '--filter', type=str, action='store', default=RAINBOW_FILTER, help="Path to custom filter image")
args = parser.parse_args()
path = args.path
alpha = args.alpha
smooth = args.smooth
filter_path = args.filter

filter = Image.open(filter_path if not smooth else RAINBOW_SMOOTH).convert('RGBA')
# we need the original pic to change alpha
filter.putalpha(alpha)

def rainbowup_file(path):
    try:
        img = Image.open(path).convert('RGBA')
        resized_filter = filter.resize(img.size)
        filename = path + '-rainbowed.png'
        Image.alpha_composite(img, resized_filter).save(filename)
        print('Rainbowed image generated at: ' + filename)
    except:
        print('Error occurred processing: ' + path)

if os.path.isfile(path):
    rainbowup_file(path)
elif os.path.isdir(path):
    images = [glob.glob(path + '/*.%s' % ext) for ext in ["jpg", "jpeg", "png"]]
    for type in images:
        for i in type:
            rainbowup_file(i)

else:
    print("The path specified does not exist")
    sys.exit()

