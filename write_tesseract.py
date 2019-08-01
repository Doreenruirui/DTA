import os
from os.path import join as pjoin
import numpy as np
from bs4 import BeautifulSoup


img_file = '/scratch/dong.r/Dataset/DTA/core_image_list_font'
data_folder = '/scratch/dong.r/Dataset/DTA'


with open(img_file, encoding='utf-8') as f_:
    files = []
    nline = 0
    dict_lang = {}
    for line in f_:
        nline += 1
        print(nline)
        font, image = line.strip().split('\t')
        if font == 'Fraktur' or font == 'Frakur':
            files.append(('frk', image))
        else:
            book = image.split('/')[2]
            if book not in dict_lang:
    
                with open(pjoin(data_folder, 'core_xml', book + '.TEI-P5.xml'), encoding='utf-8') as f_:
                    content = f_.read()
                    cur_xml = BeautifulSoup(content, 'xml')
                    lang_list = cur_xml.find_all('language')
                    cur_lang = lang_list[0]["ident"]
                    dict_lang[book] = cur_lang
            else:
                cur_lang = dict_lang[book]
            files.append((cur_lang, image))
        
nfile = len(files)
print(nfile)

chunk_size = 1000
nchunk = int(np.ceil(nfile/chunk_size))

for i in range(nchunk):
    start = i * chunk_size
    end = (i+1) * chunk_size
    with open('scripts/ocr/run.sbatch.%d' % i, 'w', encoding='utf-8') as f_:
        f_.write('#!/bin/bash\n')
        f_.write('#SBATCH --job-name=%d\n' % i)
        f_.write('#SBATCH --output=/home/dong.r/DTA/log/out.ocr.tess.%d\n' % i)
        f_.write('#SBATCH --error=/home/dong.r/DTA/log/err.ocr.tess.%d\n' % i)
        #f_.write('#SBATCH --exclusive\n')
        f_.write('#SBATCH --partition=general\n')
        f_.write('#SBATCH -N 1\n')
        f_.write('work=/home/dong.r/DTA\n')
        f_.write('cd $work\n')
        f_.write('source ~/.bash_tess\n')
        for j in range(start, end):
            ft, img = files[j]
            items = img.split('/')
            book=items[2]
            img_prefix = items[3][:-len('.png')]
            hocr_folder = pjoin(data_folder, 'core_hocr', book)
            if not os.path.exists(hocr_folder):
                os.makedirs(hocr_folder)

            f_.write('tesseract %s %s -l %s hocr\n' % (data_folder + '/' + img, data_folder + '/core_hocr/' + book + '/' + img_prefix, ft))
