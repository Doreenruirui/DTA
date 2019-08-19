import os
from os.path import join as pjoin
import numpy as np
from info import root_folder, seg_folder
from common import book2century, book2lang
import random
import sys

def get_info():
    books = os.listdir(seg_folder)
    bn2cent, bn2font = book2century()
    bn2lang = book2lang()
    cent2bn = {}
    for bn in books:
        if bn in bn2cent:
            cent = bn2cent[bn]
            if cent not in cent2bn:
                cent2bn[cent] = []
            cent2bn[cent].append(bn)
    cent2lang = {}
    cent2font = {}
    for cent in cent2bn:
        cent2lang[cent] = {}
        cent2font[cent] = {}
        books = cent2bn[cent]
        for bn in books:
            font = bn2font[bn]
            lang = bn2lang[bn]
            cent2lang[cent][lang] = cent2lang[cent].get(lang, 0) + 1
            cent2font[cent][font] = cent2font[cent].get(font, 0) + 1
    print(cent2lang)
    print(cent2font)
    for  ele in cent2bn:
        print(ele, len(cent2bn[ele]))



def split_book():
    books = os.listdir(seg_folder)
    bn2cent, bn2font = book2century()
    bn2lang = book2lang()
    centuries = ['17', '18', '19']
    frakturs = {ele: [] for ele  in centuries}
    antiquas = {ele: [] for ele  in centuries}
    for bn in books:
        if bn in bn2cent:
            cent = bn2cent[bn]
            if cent in centuries:
                font = bn2font[bn]
                lang = bn2lang[bn]
                if font == 'Fraktur' or font == 'Frakur':
                    frakturs[cent].append(bn)
                elif font == 'Antiqua' and lang == 'deu':
                    antiquas[cent].append(bn)
    for cent in frakturs:
        books = frakturs[cent]
        for i in range(5):
            random.shuffle(books)
            with open(pjoin(root_folder, 'Fraktur_%s_%d') % (cent, i), 'w', encoding='utf-8') as f_:
                for bn in books:
                    f_.write(bn + '\n')
    for cent in antiquas:
        books = antiquas[cent]
        for i in range(5):
            random.shuffle(books)
            with open(pjoin(root_folder, 'Antiqua_%s_%d') % (cent, i), 'w', encoding='utf-8') as f_:
                for bn in books:
                    f_.write(bn + '\n')

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

# def choose_lines(font, cent, start, end, split_id):
#     books = []
#     with open(pjoin(root_folder, '%s_%d_%d' % (font, cent, split_id)), encoding='utf-8') as f_:
#         for line in f_:
#             books.append(line.strip())
#     chosen_books = books[start:end]
#     all_lines = []
#     for bn in chosen_books:
#         pages = os.listdir(pjoin(seg_folder, bn))
#         for pn in pages:
#             all_lines += [(bn, pn, ele) for ele in os.listdir(pjoin(seg_folder, bn, pn)) if ele.endswith('.png')]
#     print(len(all_lines))
#     with open(pjoin(root_folder, '%s_%d_%d_%d_%d' % (font, cent, start, end, split_id)), 'w', encoding='utf-8') as f_out:
#         for line in all_lines:
#             f_out.write(pjoin(seg_folder, line[0], line[1], line[2]) + '\n')
#
# choose_lines(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
# split_book()
# get_info()




