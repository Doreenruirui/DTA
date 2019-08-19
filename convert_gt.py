from PIL import Image
import os
from os.path import join as pjoin
import json
import sys
import re

root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'


def convert_file(bn):
    pages =  os.listdir(pjoin(seg_folder, bn))
    for pn in pages:
        files = [ele for ele  in os.listdir(pjoin(seg_folder, bn, pn)) if ele.endswith('.gt.txt')]
        for fn in files:
            with open(pjoin(seg_folder, bn, pn, fn), encoding='utf-8') as f_:
                content = f_.readlines()[0].strip('\n')
                new_content = content.replace('-', '')
                new_content = new_content.replace(u"\u2010", "-")
            with open(pjoin(seg_folder, bn, pn, fn), 'w', encoding='utf-8') as f_:
                f_.write(new_content + '\n')

bookname = sys.argv[1]
convert_file(bookname)