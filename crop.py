from PIL import Image
import os
from os.path import join as pjoin
import json
import sys

root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'
filename = sys.argv[1]


def crop_file(fn):
    cur_id = ''
    line_no = 0
    f_info = open(pjoin(root_folder, 'line_info_%s' % fn), 'w', encoding='utf-8')
    print(fn)
    with open(pjoin(align_folder, fn), encoding='utf-8') as f_:
        f_lno = 0
        for line in f_:
            f_lno += 1
            print(f_lno)
            cur_line = json.loads(line)
            line_id = cur_line["id"]
            if cur_id != line_id:
                line_no = 0
                cur_id = line_id
            gt = cur_line["talg"].strip()
            ocr = cur_line["walg"].strip()
            if len(cur_line["wpages"]) == 0 or len(gt) == 0 or len(ocr) == 0:
                continue
            book_id, page_id = cur_line["wpages"][0]["id"].split('/')[-2:]
            regions = cur_line["wpages"][0]["regions"][0]["coords"]
            if len(ocr) == len(gt) and ocr[0] != '-' and ocr[-1] != '-' and gt[0] != '-' and gt[-1] != '-':
                im = Image.open(pjoin(img_folder, book_id, page_id + '.bin.png'))
                im = im.crop((regions["x"], regions["y"], regions["x"] + regions["w"], repwgions["y"] + regions["h"]))
                page_folder = pjoin(seg_folder, book_id, page_id)
                if not os.path.exists(page_folder):
                    os.makedirs(page_folder)
                im.save(pjoin(page_folder, str(line_no) + '.png'))
                with open(pjoin(page_folder, str(line_no) + '.gt.txt'), 'w', encoding='utf-8') as f_gt:
                    f_gt.write(cur_line["text"].strip('\n') + '\n')
                f_info.write('%s\t%s\t%d\t%s\t%d\n' % (book_id, page_id, line_no, fn, f_lno))
                line_no += 1
        print(f_lno)


crop_file(filename)
