from PIL import Image
from os.path import join as pjoin
import sys
import os

def get_all_files(data_folder, postfix='.png'):
    return [ele.rsplit('.', 1)[0] for ele in os.listdir(data_folder) if ele.endswith(postfix)]


def convert_image(data_folder):
    # convert image to tif
    for fn in get_all_files(data_folder):
        im = Image.open(pjoin(data_folder, fn + '.png'))
        im.save(pjoin(data_folder, fn + '.tif'))

convert_image(sys.argv[1])
