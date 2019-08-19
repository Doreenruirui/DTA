import os
from os.path import join as pjoin


root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'

files = [ele for ele in os.listdir(align_folder) if ele.startswith('part-')]
nfile = len(files)

for i in range(nfile):
    with open('scripts/crop/run.sbatch.%d' % i, 'w', encoding='utf-8') as f_:
        f_.write('#!/bin/bash\n')
        f_.write('#SBATCH --job-name=%d\n' % i)
        f_.write('#SBATCH --output=/home/dong.r/DTA/log/out.crop.%d\n' % i)
        f_.write('#SBATCH --error=/home/dong.r/DTA/log/err.crop.%d\n' % i)
        # f_.write('#SBATCH --exclusive\n')
        f_.write('#SBATCH --partition=general\n')
        f_.write('#SBATCH -N 1\n')
        f_.write('work=/home/dong.r/DTA\n')
        f_.write('cd $work\n')
        f_.write('python crop.py %s\n' % files[i])
