import os
from os.path import join as pjoin


root_folder = '/scratch/dong.r/Dataset/DTA'
img_folder = root_folder + '/core_image'
align_folder = root_folder + '/out.json'
seg_folder = root_folder + '/core_segment'

books = [ele for ele in os.listdir(seg_folder)]
i = 0
for bn in  books:
    pages = os.listdir(pjoin(seg_folder, bn))
    with open('scripts/binarize/run.sbatch.%d' % i, 'w', encoding='utf-8') as f_:
        f_.write('#!/bin/bash\n')
        f_.write('#SBATCH --job-name=%d\n' % i)
        f_.write('#SBATCH --output=/home/dong.r/DTA/log/out.bin.%d\n' % i)
        f_.write('#SBATCH --error=/home/dong.r/DTA/log/err.bin.%d\n' % i)
        f_.write('#SBATCH --partition=general\n')
        f_.write('#SBATCH -N 1\n')
        f_.write('work=/home/dong.r/DTA\n')
        f_.write('cd $work\n')
        f_.write('source activate kraken\n')
        for pn in pages:
            lines = [ele for ele in os.listdir(pjoin(seg_folder, bn, pn)) if ele.endswith('.png')]
            for img in lines:
                img_name = img[:-len('.png')]
                img_path = pjoin(seg_folder, bn, pn, img_name)
                f_.write('kraken -i %s.png %s.bin.png binarize\n' %  (img_path, img_path))
                f_.write('rm %s.png\n' %  img_path)
        i += 1

