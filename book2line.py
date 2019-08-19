import sys
import os
from os.path import join as pjoin
from info import root_folder, seg_folder


def book2lines(bn):
    all_lines = []
    pages = sorted(os.listdir(pjoin(seg_folder, bn)))
    for pn in pages:
        all_lines += [(bn, pn, ele) for ele in sorted(os.listdir(pjoin(seg_folder, bn, pn))) if ele.endswith('.png')]
    print(len(all_lines))
    book_info_folder = pjoin(root_folder, 'book_info')
    if not os.path.exists(book_info_folder):
        os.makedirs(book_info_folder)
    with open(pjoin(book_info_folder, bn), 'w', encoding='utf-8') as f_bn:
        f_bn.write(str(len(all_lines)) +  '\n')
        for line in all_lines:
            f_bn.write(pjoin(seg_folder, line[0], line[1], line[2]) + '\n')

book2lines(sys.argv[1])