from PIL import Image
import numpy as np
import os
import shutil

root_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = newPath = root_dir.replace(os.sep, '/')

jpg_path = root_dir + "/jpg"
bmp_path = root_dir + "/bmp"
#png_path = root_dir + "/png"

#turn jpg to grayscale and save as .bmp
def to_png(path, png_name, bmp_name):
    img = Image.open(path).convert('LA')
    img.save(png_name)
    os.rename(png_name, bmp_name)

    

for filename in os.listdir(jpg_path):
    img_path = jpg_path + '/' + filename

    png_name = filename.replace("jpg", "png")
    bmp_name = filename.replace("jpg", "bmp")
    png_fn = bmp_path + '/' + png_name
    bmp_fn = bmp_path + '/' + bmp_name
    print("converting:", filename)
    
    to_png(img_path, png_fn, bmp_fn)
