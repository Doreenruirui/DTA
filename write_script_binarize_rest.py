import os
from os.path import join as pjoin
import numpy as np


root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'

books = [ele for ele in os.listdir(seg_folder)]

i = 0
for bn in  books:
    pages = os.listdir(pjoin(seg_folder, bn))
    if os.path.exists(pjoin(seg_folder,  bn,  pages[0], '0.bin.png')):
        continue
    all_lines  = []
    for pn in pages:
        all_lines += [(pn, ele) for ele in os.listdir(pjoin(seg_folder, bn, pn)) if ele.endswith('.png')]
    chunk_size = 3000
    nline = len(all_lines)
    nchunk = int(np.ceil(nline/chunk_size))
    for j in range(nchunk):
        start = chunk_size  * j
        end = min(chunk_size  +  start,  nline)
        with open('scripts/binarize_rest/run.sbatch.%d' % i, 'w', encoding='utf-8') as f_:
            f_.write('#!/bin/bash\n')
            f_.write('#SBATCH --job-name=%d\n' % i)
            f_.write('#SBATCH --output=/home/dong.r/DTA/log/out.bin.rest.%d\n' % i)
            f_.write('#SBATCH --error=/home/dong.r/DTA/log/err.bin.rest.%d\n' % i)
            f_.write('#SBATCH --partition=general\n')
            f_.write('#SBATCH -N 1\n')
            f_.write('work=/home/dong.r/DTA\n')
            f_.write('cd $work\n')
            f_.write('source activate kraken\n')
            for k in range(start, end):
                pn, img  = all_lines[k]
                img_name = img[:-len('.png')]
                img_path = pjoin(seg_folder, bn, pn, img_name)
                f_.write('kraken -i %s.png %s.bin.png binarize\n' %  (img_path, img_path))
                f_.write('rm %s.png\n' %  img_path)
        i += 1

