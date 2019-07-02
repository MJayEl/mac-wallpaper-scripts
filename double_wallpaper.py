#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from PIL import Image
import sys
import os

MON_WIDTH = 1920
MON_HEIGHT = 1080

if len(sys.argv) == 1:
    print('ERROR: Must include image path as second arg')
else:
    image_name = sys.argv[1]
    #check for relative or absolute path (if relative add current dir for applescript)
    if not os.path.isabs(image_name):
        image_name = os.path.join(os.getcwd(),image_name)
    ext = '.'+image_name.split('.')[1]
    im = Image.open(image_name)
    width, height = im.size
    half_width = width/2

    area1 = (0,0,half_width, height)         
    area2 = (half_width, 0, width, height)   
    #if width is greater than 2 monitor widths get image center so that it doesn't look off center
    if width > (MON_WIDTH * 2):
        area1 = (half_width - MON_WIDTH,0, half_width, height) 
  
    #crop images 
    im1 = im.crop(area1)
    im2 = im.crop(area2)
    #make names e.g. _0_1.jpg and _0_2.jpg
    path = os.getcwd()
    filename = os.path.basename(image_name)
    im1_name = os.path.join(path, '._'+filename.split('.')[0])+'_1'+ext
    im2_name = os.path.join(path, '._'+filename.split('.')[0])+'_2'+ext
    im1.save(im1_name)
    im2.save(im2_name)
    #use applescript to set backgrounds
    os.system("osascript -e 'tell application \"System Events\" to set picture of desktop 1 to \"{}\"'".format(im1_name))
    os.system("osascript -e 'tell application \"System Events\" to set picture of desktop 2 to \"{}\"'".format(im2_name))
