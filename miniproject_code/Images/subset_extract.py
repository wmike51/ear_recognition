import os
import shutil

from isort import file
root_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = newPath = root_dir.replace(os.sep, '/')

# change subset filename
dir_path = root_dir + "/subset-4"

# print(os.listdir(dir_path))
jpg_path = root_dir + "/jpg"
for filename in os.listdir(dir_path):
    # extract only front samples
    if "back" in filename:
        img_path = dir_path + '/' + filename
        # print(path)
        shutil.copy(img_path, jpg_path)
        new_name = filename.replace("back_ear", "1")
        os.rename(jpg_path + '/' + filename, jpg_path + '/' + new_name)

    if "down" in filename:
        img_path = dir_path + '/' + filename
        # print(path)
        shutil.copy(img_path, jpg_path)
        new_name = filename.replace("down_ear", "2")
        os.rename(jpg_path + '/' + filename, jpg_path + '/' + new_name)

    if "front" in filename:
        img_path = dir_path + '/' + filename
        # print(path)
        shutil.copy(img_path, jpg_path)
        new_name = filename.replace("front_ear", "3")
        os.rename(jpg_path + '/' + filename, jpg_path + '/' + new_name)

    if "left" in filename:
        img_path = dir_path + '/' + filename
        # print(path)
        shutil.copy(img_path, jpg_path)
        new_name = filename.replace("left_ear", "4")
        os.rename(jpg_path + '/' + filename, jpg_path + '/' + new_name)

    if "right" in filename:
        img_path = dir_path + '/' + filename
        # print(path)
        shutil.copy(img_path, jpg_path)
        new_name = filename.replace("right_ear", "5")
        os.rename(jpg_path + '/' + filename, jpg_path + '/' + new_name)

    if "up" in filename:
        img_path = dir_path + '/' + filename
        # print(path)
        shutil.copy(img_path, jpg_path)
        new_name = filename.replace("up_ear", "6")
        os.rename(jpg_path + '/' + filename, jpg_path + '/' + new_name)

    if "zoom" in filename:
        img_path = dir_path + '/' + filename
        # print(path)
        shutil.copy(img_path, jpg_path)
        new_name = filename.replace("zoom_ear", "7")
        os.rename(jpg_path + '/' + filename, jpg_path + '/' + new_name)
