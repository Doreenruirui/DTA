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

def get_unfinished():
    unfinished = {}
    books = os.listdir(seg_folder)
    for bn in books:
        pages = os.listdir(pjoin(seg_folder, bn))
        for pg in pages:
            lines = [ele[:-len('.gt.txt')] for ele in os.listdir(pjoin(seg_folder, bn, pg)) if ele.endswith('.gt.txt')]
            for ele in lines:
                if not os.path.exists(pjoin(seg_folder, bn, pg, ele + '.bin.png')):
                    if not os.path.exists(pjoin(seg_folder, bn, pg, ele + '.png')):
                        unfinished[(bn, pg, ele)] = 1

    dict_file2line = {}
    dict_file2imgno = {}
    with open(pjoin(root_folder, 'line_info'), encoding='utf-8') as f_:
        for line in f_:
            bn, pg, lno, jsonfile, json_lno = line.strip().split('\t')
            if (bn, pg, lno) in unfinished:
                dict_file2line[jsonfile] = json_lno
                dict_file2imgno[jsonfile] = lno

    for ele in dict_file2line:
        with open(pjoin(root_folder, 'unfinished_%s' % ele), 'w') as f_out:
            f_out.write(ele + ',' + '\t'.join(dict_file2line[ele]) + ',' + '\t'.join(dict_file2imgno[ele]) + '\n')


get_unfinished()
#
# def crop_unfinished(fn):
#     with open(pjoin(root_folder,'unfinished')) as f_:
#         for line in f_:
#             items = line.strip().split('\t')
#             filename = items[0]
#             if filename == fn:
#                 list_lno = {int(ele): 1 for ele in items[1:]}
#                 with open(pjoin(align_folder, fn), encoding='utf-8') as f_:
#                     f_lno = 0
#                     for line in f_:
#                         f_lno += 1
#                         if f_lno in list_lno:
#                             cur_line  = json.loads(line)
#                             book_id, page_id = cur_line["wpages"][0]["id"].split('/')[-2:]
#                             regions = cur_line["wpages"][0]["regions"][0]["coords"]
#                             im = Image.open(pjoin(img_folder, book_id, page_id + '.png'))
#                             im = im.crop((regions["x"], regions["y"], regions["x"] + regions["w"], regions["y"] + regions["h"]))
#                             page_folder = pjoin(seg_folder, book_id, page_id)
#                             im.save(pjoin(page_folder, str(line_no) + '.png'))
#
