import os
from os.path import join as pjoin


root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'

books = [ele for ele in os.listdir(seg_folder)]
i = 0
for bn in  books:
    with open('scripts/count_book/run.sbatch.%d' % i, 'w', encoding='utf-8') as f_:
        f_.write('#!/bin/bash\n')
        f_.write('#SBATCH --job-name=%d\n' % i)
        f_.write('#SBATCH --output=/home/dong.r/DTA/log/out.count.book.%d\n' % i)
        f_.write('#SBATCH --error=/home/dong.r/DTA/log/err.count.book.%d\n' % i)
        f_.write('#SBATCH --partition=general\n')
        f_.write('#SBATCH -N 1\n')
        f_.write('work=/home/dong.r/DTA\n')
        f_.write('cd $work\n')
        f_.write('python book2line.py %s\n' % bn)
    i += 1
