import os
from os.path import join as pjoin


root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'
list_tuples = [('Fraktur', 17, 0, 150),
               ('Fraktur', 17, 150, 200),
               ('Fraktur', 18, 0, 150),
               ('Fraktur', 18, 0, 300),
               ('Fraktur', 18, 300, 350),
               ('Fraktur', 19, 0, 150),
               ('Fraktur', 19, 0, 300),
               ('Fraktur', 19, 300, 350),
               ('Antiqua', 18, 0, 20),
               ('Antiqua', 19, 0, 150),
               ('Antiqua', 19, 150, 170)]

i = 0
for item in list_tuples:
    for split_id  in range(3):
        with open('scripts/split_book/run.sbatch.%d' % i, 'w', encoding='utf-8') as f_:
            f_.write('#!/bin/bash\n')
            f_.write('#SBATCH --job-name=%d\n' % i)
            f_.write('#SBATCH --output=/home/dong.r/DTA/log/out.split.book.%d\n' % i)
            f_.write('#SBATCH --error=/home/dong.r/DTA/log/err.split.book.%d\n' % i)
            f_.write('#SBATCH --partition=general\n')
            f_.write('#SBATCH -N 1\n')
            f_.write('work=/home/dong.r/DTA\n')
            f_.write('cd $work\n')
            f_.write('python choose_lines.py %s %d %d %d %d\n' % (item[0], item[1], item[2], item[3], split_id))
        i += 1
